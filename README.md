# 🕌 Islamic Screener

Un outil éducatif en **finance islamique** permettant d’évaluer si une action cotée est **halal**, **tolérable**, ou **non conforme** selon les standards **AAOIFI**, **DJIM** et **MSCI**.

---

## ⚙️ Fonctionnalités

- 🧭 **Filtrage sectoriel automatique** (détection des secteurs haram)
- 📊 **Calcul des ratios financiers AAOIFI**
  - Dette / Capitalisation
  - Trésorerie à intérêt / Capitalisation
  - Revenus non conformes estimés
- ✅ **Verdict automatique** : conforme, tolérable ou non conforme
- 🖥️ **Graphique TradingView intégré**
- 🧩 **Bandeau défilant de marché en direct** (actions conformes halal)
- 📚 Explication intégrée sur la **purification des revenus haram**

---

## 🧮 Règles de conformité (AAOIFI)

### 1️⃣ Filtre sectoriel (absolu)
Les entreprises exerçant dans les domaines suivants sont **automatiquement non conformes** :
- Banques / Assurances (riba)
- Alcool
- Jeux d’argent
- Tabac
- Porc
- Armement offensif
- Divertissement immoral

### 2️⃣ Ratios financiers
| Critère | Seuil AAOIFI | Interprétation |
|----------|---------------|----------------|
| Dette / Capitalisation | < 30 % | Trop de dettes → Non conforme |
| Trésorerie à intérêt / Capitalisation | < 30 % | Trop de placements à intérêt → Non conforme |
| Revenus non conformes / CA | ≤ 5 % | Si >5 % → Non conforme |

---

## 📘 Comment estimer les revenus non conformes

Les revenus non conformes proviennent d’activités interdites (intérêts, alcool, jeux, etc.).

**Méthode AAOIFI :**
1️⃣ Identifier dans le rapport financier les sources de revenus haram (ex: intérêts bancaires).  
2️⃣ Calculer :  
   > **(Revenus haram / Revenus totaux) × 100**
3️⃣ Si ce ratio ≤ 5 %, l’action est **tolérable**.  
4️⃣ Au-delà de 5 %, elle devient **non conforme**.  
5️⃣ En cas de tolérance, il faut **purifier** cette part en **donnant en aumône** le même pourcentage des dividendes perçus.

**Exemple :**  
Si une société tire 2 % de ses revenus d’intérêts →  
→ Action **tolérable**, mais il faut purifier **2 % des dividendes**.

---

## 🧾 Exemple d’utilisation

| Étape | Description |
|-------|--------------|
| 1 | Lancer l’application |
| 2 | Entrer un **ticker** (ex: `AAPL`, `MSFT`, `NVDA`, `NVO`, `PG`) |
| 3 | Consulter les ratios et le verdict |
| 4 | Vérifier le graphique TradingView en fin de page |

---

## 🚀 Installation locale

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/tonpseudo/islamic-screener.git
cd islamic-screener
