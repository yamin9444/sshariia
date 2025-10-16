#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import yfinance as yf

# --------------------------
# CONFIGURATION DE LA PAGE
# --------------------------
st.set_page_config(page_title="Islamic Screener", page_icon="🕌", layout="wide")

# --------------------------
# BANDEAU DÉFILANT TRADINGVIEW (avec logos + 3 nouvelles sociétés)
# --------------------------
st.markdown("""
<!-- Bandeau défilant TradingView -->
<iframe src="https://s.tradingview.com/embed-widget/ticker-tape/?locale=fr#%7B%22symbols%22%3A%5B
%7B%22proName%22%3A%22NASDAQ%3AAAPL%22%2C%22title%22%3A%22Apple%22%7D%2C
%7B%22proName%22%3A%22NASDAQ%3AMSFT%22%2C%22title%22%3A%22Microsoft%22%7D%2C
%7B%22proName%22%3A%22NYSE%3ANVO%22%2C%22title%22%3A%22Novo%20Nordisk%22%7D%2C
%7B%22proName%22%3A%22NYSE%3AJNJ%22%2C%22title%22%3A%22Johnson%20%26%20Johnson%22%7D%2C
%7B%22proName%22%3A%22NYSE%3APG%22%2C%22title%22%3A%22Procter%20%26%20Gamble%22%7D%2C
%7B%22proName%22%3A%22NASDAQ%3ANKE%22%2C%22title%22%3A%22Nike%22%7D%2C
%7B%22proName%22%3A%22NYSE%3AINTC%22%2C%22title%22%3A%22Intel%22%7D%2C
%7B%22proName%22%3A%22NASDAQ%3ANVDA%22%2C%22title%22%3A%22Nvidia%22%7D
%5D%2C%22showSymbolLogo%22%3Atrue%2C%22colorTheme%22%3A%22light%22%2C%22isTransparent%22%3Afalse%2C%22displayMode%22%3A%22adaptive%22%2C%22width%22%3A%22100%25%22%2C%22height%22%3A%2240%22%7D"
width="100%" height="40" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
""", unsafe_allow_html=True)

# --------------------------
# TITRE PRINCIPAL
# --------------------------
st.markdown("<h1 style='text-align:center;'>🕌 Islamic Screener</h1>", unsafe_allow_html=True)
st.write("**But :** filtrer rapidement une action selon la *finance islamique* (AAOIFI / DJIM / MSCI).")

# --------------------------
# RÈGLES D’INVESTISSEMENT
# --------------------------
st.markdown("""
## 📜 Règles pour investir halal

### 1️⃣ Filtre sectoriel (absolu)
❌ Exclure : banques, assurances (riba), alcool, jeux d'argent, tabac, porc, armement offensif, divertissement immoral.  
Si le secteur est haram → **non conforme directe**.

---

### 2️⃣ Ratios financiers (AAOIFI)
- Dette / Capitalisation **< 30 %**  
- Trésorerie à intérêt / Capitalisation **< 30 %**  
- Revenus non conformes / Chiffre d’affaires **≤ 5 %**

---

### 📊 Comment estimer les **revenus non conformes**
Les revenus non conformes proviennent d’activités interdites selon la Shariah (riba, alcool, jeux, etc.).  
L’AAOIFI recommande la méthode suivante :

1️⃣ Identifier les **sources de revenus haram** dans les rapports financiers (intérêts, investissements, activités interdites).  
2️⃣ Calculer le **pourcentage** :  
   **(Revenus haram / Revenus totaux)** × 100  
3️⃣ Si ce pourcentage ≤ 5 %, l’action reste **tolérable**, sinon elle est **non conforme**.  
4️⃣ En cas de tolérance (moins de 5 %), l’investisseur doit **purifier** cette partie en la **donnant en aumône** (sans intention de sadaqa volontaire).

Exemple :  
Si une société a 2 % de ses revenus provenant d’intérêts bancaires →  
→ elle est **conforme**, mais nécessite une **purification** de 2 % des dividendes perçus.

---

### 3️⃣ Verdict final :
- ✅ Tous bons → **Conforme (Halal)**  
- ⚠️ Limite → **Tolérable (à purifier)**  
- ❌ Dépassement → **Non conforme**
""")

# --------------------------
# INPUT DU TICKER
# --------------------------
ticker = st.text_input("🔎 Entrez le ticker (ex: AAPL, MSFT, NVO, PG, JNJ, NKE, INTC, NVDA) :").upper()

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        st.markdown(f"## {info.get('shortName', ticker)} ({ticker})")
        st.write(f"Secteur : **{info.get('sector', 'N/A')}** | Industrie : **{info.get('industry', 'N/A')}** | "
                 f"Capitalisation : **{info.get('marketCap', 'N/A'):,} $**")

        # --------------------------
        # RATIOS SIMPLIFIÉS
        # --------------------------
        total_debt = info.get("totalDebt", 0)
        market_cap = info.get("marketCap", 1)
        cash = info.get("totalCash", 0)

        debt_cap = (total_debt / market_cap) * 100
        cash_cap = (cash / market_cap) * 100
        haram_rev = 0.0  # valeur par défaut (à estimer manuellement si connue)

        # --------------------------
        # ÉVALUATION DE CONFORMITÉ
        # --------------------------
        status = "✅ Conforme (Halal)"
        color = "green"
        if "Bank" in info.get("sector", "") or "Financial" in info.get("sector", ""):
            status = "❌ Non conforme (Secteur financier)"
            color = "red"
        elif debt_cap > 30 or cash_cap > 30 or haram_rev > 5:
            status = "❌ Non conforme (Ratios dépassés)"
            color = "red"
        elif 25 < debt_cap < 30 or 25 < cash_cap < 30 or 4 < haram_rev < 5:
            status = "⚠️ Tolérable"
            color = "orange"

        st.markdown(f"<h3 style='color:{color};'>{status}</h3>", unsafe_allow_html=True)

        # --------------------------
        # DÉTAILS DES RATIOS
        # --------------------------
        st.markdown("### 💹 Ratios Financiers (AAOIFI)")
        st.write(f"**Dette / Capitalisation :** {debt_cap:.2f}%")
        st.write(f"**Cash / Capitalisation :** {cash_cap:.2f}%")
        st.write(f"**Revenus non conformes estimés :** {haram_rev:.2f}%")
        st.caption("📘 Seuils AAOIFI : Dette <30 %, Cash <30 %, Revenus haram <5 %")

        # --------------------------
        # GRAPHIQUE TRADINGVIEW
        # --------------------------
        st.markdown("## 📊 Graphique TradingView (temps réel)")
        st.markdown(f"""
        <iframe src="https://s.tradingview.com/widgetembed/?symbol={ticker}&interval=D&hidesidetoolbar=1&theme=light"
        width="100%" height="500" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
        """, unsafe_allow_html=True)

        st.info("⚠️ Application éducative — ne constitue pas un avis Shariah officiel.")
    
    except Exception as e:
        st.error(f"Erreur : impossible de récupérer les données pour {ticker}. ({e})")

else:
    st.info("🔹 Entrez un ticker ci-dessus pour analyser la conformité islamique.")

