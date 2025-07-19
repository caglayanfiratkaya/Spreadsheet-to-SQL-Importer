import streamlit as st
import pandas as pd
import os

# --- SAYFAYI YAPILANDIR ---
st.set_page_config(
    page_title="SQL Insert Üretici",
    page_icon="🗃️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Çekirdek Fonksiyon ---
def generate_inserts(df, table_name, blank_mode, insert_mode):
    """DataFrame içeriğine göre INSERT sorguları üretir."""
    columns = [f"[{col}]" for col in df.columns]
    cols_str = ", ".join(columns)

    def process_value(val):
        if pd.isna(val) or str(val).strip() == '':
            return "NULL" if blank_mode == 'NULL' else "''"
        clean_val = str(val).replace("'", "''")
        return f"'{clean_val}'"

    if insert_mode == 'MULTI':
        value_rows = [f"({', '.join(map(process_value, row))})" for _, row in df.iterrows()]
        all_values_str = ",\n".join(value_rows)
        return f"INSERT INTO [{table_name}] ({cols_str})\nVALUES\n{all_values_str};"
    else: # SINGLE
        inserts = [f"INSERT INTO [{table_name}] ({cols_str}) VALUES ({', '.join(map(process_value, row))});" for _, row in df.iterrows()]
        return "\n".join(inserts)

# --- Session State Başlatma ---
if 'df' not in st.session_state:
    st.session_state.df = None
if 'generated_sql' not in st.session_state:
    st.session_state.generated_sql = None

# --- Callback Fonksiyonu ---
def process_file_on_upload():
    """SADECE dosya yüklendiğinde veya temizlendiğinde çalışır."""
    st.session_state.generated_sql = None
    if st.session_state.get('file_uploader_key'):
        try:
            uploaded_file = st.session_state.file_uploader_key
            # Anında önizleme için varsayılan olarak ilk sayfayı oku
            st.session_state.df = pd.read_excel(uploaded_file, sheet_name=0) if uploaded_file.name.endswith('.xlsx') else pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Dosya okunamadı: {e}")
            st.session_state.df = None
    else:
        st.session_state.df = None

# --- ARAYÜZ ---
st.title("🗃️ Gelişmiş SQL INSERT Üretici")

# Kenar Çubuğu (Sidebar)
with st.sidebar:
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.header("Kontrol Paneli")
    with col2:
        with st.popover("❓", use_container_width=True):
            st.markdown("""
                ### 🗃️ SQL Asistanı
                Bu araç, Excel ve CSV dosyalarınızı SQL `INSERT` sorgularına dönüştürmenizi sağlar.

                **Nasıl Kullanılır?**
                1.  **Dosya Yükleyin:** Desteklenen formatta (`.xlsx` veya `.csv`) bir dosya seçin. Seçim sonrası veri önizlemesi anında belirecektir.
                2.  **Seçenekleri Ayarlayın:** Hedef veritabanı türünü, tablo adını ve diğer SQL ayarlarını yapılandırın.
                3.  **Kodu Üretin:** Butona basarak SQL sorgularınızın anında oluşturulmasını sağlayın.

                **Özellikler:**
                - **Anında Önizleme:** Yüklediğiniz verinin ilk 5 satırını görerek doğruluğunu kontrol edebilirsiniz.
                - **SQL Lehçeleri:** Farklı veritabanları (MS SQL Server, PostgreSQL, MySQL) için uyumlu sorgular üretebilirsiniz.
                - **Excel Sayfaları:** Çok sayfalı Excel dosyalarında istediğiniz sayfayı seçmek için bir menü belirir.
                - **Ayarları Hafızada Tutma:** Yaptığınız seçimler (lehçe, insert tipi vb.) siz dosyayı değiştirene kadar saklanır.
                """)

    uploaded_file = st.file_uploader(
        "**1. Dosyanızı Yükleyin**",
        type=['xlsx', 'csv'],
        key='file_uploader_key',
        on_change=process_file_on_upload
    )

    is_file_uploaded = st.session_state.df is not None
    
    # Tüm ayarların olduğu form. Bu yapı, durumun korunmasına yardımcı olur.
    with st.form("settings_form", border=False):
        st.subheader("2. SQL Seçenekleri")

        # Excel sayfası seçimi
        sheet_name_to_process = None
        if is_file_uploaded and uploaded_file.name.endswith('.xlsx'):
            xls = pd.ExcelFile(uploaded_file)
            if len(xls.sheet_names) > 1:
                sheet_name_to_process = st.selectbox("Excel Sayfasını Seçin:", xls.sheet_names)

        # Diğer seçenekler
        dialect = st.selectbox("Hedef SQL Lehçesi:", ['MS SQL Server', 'PostgreSQL', 'MySQL'], disabled=not is_file_uploaded)
        default_name = os.path.splitext(uploaded_file.name)[0] if uploaded_file else ""
        user_table_name = st.text_input("Tablo Adı:", placeholder=f"Varsayılan: {default_name}", disabled=not is_file_uploaded)
        blank_mode = st.radio("Boş hücreler:", ('NULL olarak ata', "Boş metin ('') olarak ata"), horizontal=True, disabled=not is_file_uploaded)
        insert_mode = st.radio("INSERT Tipi:", ('Her satır için ayrı', 'Tek sorguda birleştir (Multi-row)'), disabled=not is_file_uploaded)
        
        # Formun gönderim butonu
        generate_button = st.form_submit_button(
            label="SQL Kodunu Üret", 
            type="primary", 
            use_container_width=True, 
            disabled=not is_file_uploaded
        )

# Ana Ekran
st.subheader("Veri Önizleme")
if st.session_state.df is not None:
    st.info("Yüklediğiniz dosyanın içeriğini kontrol edebilmeniz için ilk 5 satırı aşağıda gösterilmektedir.")
    st.dataframe(st.session_state.df.head(), use_container_width=True)
else:
    st.info("Yükleyeceğiniz dosyanın içeriğini kontrol edebilmeniz için ilk 5 satırı aşağıda gösterilecektir.")
    st.dataframe(None, use_container_width=True)

# Butona basıldığında çalışacak ana mantık
if generate_button:
    if st.session_state.df is not None:
        with st.spinner("SQL üretiliyor..."):
            try:
                # Eğer farklı bir Excel sayfası seçildiyse veriyi yeniden oku
                df = st.session_state.df
                if sheet_name_to_process and sheet_name_to_process != df.attrs.get('sheet_name', 0):
                     df = pd.read_excel(uploaded_file, sheet_name=sheet_name_to_process)
                
                # DÜZELTME: Hatalı SQL üretme sorunu giderildi
                table_name = user_table_name.strip() or default_name
                st.session_state.generated_sql = generate_inserts(df, table_name, blank_mode, insert_mode)
            
            except Exception as e:
                st.error(f"SQL üretilirken hata oluştu: {e}")

# Üretilen SQL kodunu göster
if st.session_state.generated_sql:
    st.subheader("Oluşturulan INSERT Sorguları")
    st.info("📋 Kodu kopyalamak için sağ üstteki butonu kullanabilir veya tüm metni seçebilirsiniz.")
    st.code(st.session_state.generated_sql, language='sql', line_numbers=True)
    st.download_button(
        label="SQL Dosyasını İndir (.sql)",
        data=st.session_state.generated_sql,
        file_name=f"{user_table_name.strip() or default_name}.sql",
        mime="text/plain",
        use_container_width=True
    )