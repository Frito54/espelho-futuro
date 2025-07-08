import streamlit as st
import openai

# CONFIGURE SUA CHAVE DA OPENAI AQUI 👇
openai.api_key = "SUA_CHAVE_DA_API"

st.set_page_config(page_title="Espelho Futuro IA", layout="wide")
st.title("🔮 Espelho Futuro com IA")

st.markdown("""
Responda às perguntas abaixo com sinceridade. Elas foram criadas para entender **quem você é de verdade**, de forma indireta.

A IA vai analisar suas respostas e gerar **3 versões possíveis do seu futuro** com base em desejos ocultos, medos e ambições que você talvez nem saiba que tem.
""")

# FORMULÁRIO DE PERGUNTAS PSICOLÓGICAS DISFARÇADAS
with st.form("questionario"):
    genero_filme = st.selectbox("1. Se sua vida fosse um filme, qual seria o gênero?", 
                                 ["Comédia", "Drama", "Ação", "Suspense", "Ficção", "Romance", "Documentário"])

    jantar = st.text_area("2. Jantar com 3 pessoas que você admira. Quem são e o que perguntaria?")

    botao_reiniciar = st.text_input("3. Você teria coragem de reiniciar sua vida? Em que ponto e por quê?")

    premio = st.text_area("4. Você ganhou 1 milhão de reais (sem poder investir). O que faria com esse dinheiro?")

    sem_trabalho = st.text_input("5. Se você fosse impedido de trabalhar por 2 anos, como reagiria emocionalmente?")

    cheiro_vida = st.text_input("6. Se sua vida tivesse um cheiro, qual seria? Por quê?")

    abandono = st.text_input("7. Qual foi a última coisa que você desistiu sem perceber?")

    animal_gaiola = st.text_input("8. Você é um animal selvagem preso numa gaiola de ouro. Qual sua reação?")

    evitado = st.text_input("9. O que você sabe que precisa fazer, mas evita há muito tempo?")

    energia = st.text_input("10. Se alguém descrevesse sua energia atual, o que diriam?")

    enviar = st.form_submit_button("🔍 Simular Meu Futuro")

# PROCESSAMENTO COM IA
if enviar:
    with st.spinner("Analisando sua mente com IA..."):

        respostas = f"""
        1. Gênero do filme: {genero_filme}
        2. Jantar com 3 pessoas: {jantar}
        3. Botão de reinício: {botao_reiniciar}
        4. O que faria com 1 milhão: {premio}
        5. Reação ao ficar 2 anos sem trabalhar: {sem_trabalho}
        6. Cheiro da vida: {cheiro_vida}
        7. Coisa abandonada: {abandono}
        8. Reação como animal em gaiola de ouro: {animal_gaiola}
        9. O que evita: {evitado}
        10. Energia atual: {energia}
        """

        prompt = f"""
        Você é um analista psicológico e simulador de futuros possíveis. Analise profundamente as respostas abaixo, identifique padrões emocionais, crenças ocultas, desejos e conflitos internos.

        Com base nisso, crie 3 possíveis caminhos futuros:
        1. Caminho Conservador (seguro)
        2. Caminho Transformador (mudança estratégica)
        3. Caminho Radical (desconhecido, mas libertador)

        Para cada caminho, forneça:
        - Benefícios esperados
        - Obstáculos prováveis
        - Estado emocional dominante
        - Aconselhamento racional
        - Aconselhamento do 'Eu do Futuro'

        Respostas da pessoa:
        {respostas}
        """

        try:
            resposta = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8,
                max_tokens=1200
            )
            conteudo = resposta["choices"][0]["message"]["content"]
            st.success("✨ Simulação concluída!")
            st.markdown("## 🧠 Seus 3 caminhos possíveis:")
            st.markdown(conteudo)

        except Exception as e:
            st.error(f"Erro ao acessar a IA: {str(e)}")
