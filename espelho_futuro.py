import streamlit as st
import openai

# Configurar chave via Streamlit Secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Espelho do Futuro com IA", page_icon="🔮")
st.title("🔮 Espelho do Futuro com IA")

st.markdown("Simule possibilidades de vida baseadas em sua personalidade, emoções e desejos futuros. Responda com sinceridade para insights reais.")

# Coleta de dados
with st.form("simulador_form"):
    idade = st.slider("📅 Sua idade:", 15, 80, 30)
    profissao = st.text_input("💼 Qual sua profissão atual?")
    estado_emocional = st.selectbox("🧠 Como você se sente hoje?", ["Motivado", "Ansioso", "Desanimado", "Confuso", "Curioso"])
    objetivo = st.text_area("🎯 Descreva um objetivo de vida que você gostaria de alcançar:")

    enviado = st.form_submit_button("🔍 Simular Meu Futuro")

if enviado:
    # Prompt estruturado
    prompt = f"""
    Aja como um Simulador de Futuro baseado na seguinte pessoa:
    - Idade: {idade}
    - Profissão atual: {profissao}
    - Estado emocional atual: {estado_emocional}
    - Desejo futuro: {objetivo}

    Gere 3 caminhos de vida possíveis nos próximos 2 anos:
    Para cada caminho, inclua:
    - Benefícios e conquistas
    - Desvantagens e desafios
    - Resultado provável
    - Aconselhamento racional
    - Aconselhamento emocional

    Finalize com uma reflexão: "Se você pudesse conversar com seu Eu do Futuro, o que ele te diria agora?"
    """

    # Chamada para a IA
    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",  # ou gpt-4 se você tiver
            messages=[{"role": "user", "content": prompt}]
        )

        st.subheader("🧭 Possíveis Caminhos para Seu Futuro")
        st.markdown(resposta.choices[0].message.content)

    except Exception as e:
        st.error(f"❌ Erro ao acessar a IA: {str(e)}")
