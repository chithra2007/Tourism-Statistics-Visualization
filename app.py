import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Tourism Statistics Visualization Portal",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# SESSION STATE
# =========================================================

if "started" not in st.session_state:
    st.session_state.started = False


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}


/* ================= WELCOME PAGE ================= */

.welcome-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-top: 40px;
    margin-bottom: 10px;
}

.welcome-subtitle {
    text-align: center;
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 25px;
}

.welcome-text {
    text-align: center;
    font-size: 17px;
    line-height: 1.7;
    max-width: 850px;
    margin: auto;
}


/* ================= FEATURE CARDS ================= */

.feature-box {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 15px;
    min-height: 130px;
}

.feature-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}

.feature-text {
    font-size: 15px;
    line-height: 1.5;
}


/* ================= BUTTON ================= */

div.stButton > button {
    width: 250px;
    height: 50px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 700;
}


/* ================= KPI CARDS ================= */

.kpi-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.kpi-title {
    font-size: 15px;
    font-weight: 600;
}

.kpi-value {
    font-size: 28px;
    font-weight: 800;
    margin-top: 8px;
}


/* ================= INSIGHT BOX ================= */

.insight-box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}


/* ================= FOOTER ================= */

.footer {
    text-align: center;
    margin-top: 40px;
    padding: 20px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# WELCOME PAGE
# =========================================================

if not st.session_state.started:

    st.markdown(
        '<div class="welcome-title">🌍 Tourism Statistics Visualization Portal</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="welcome-subtitle">Explore Tourism Data Through Interactive Visualizations</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="welcome-text">
            <h3>Welcome to the Tourism Statistics Visualization Portal.</h3>

            <p>
            This portal helps users analyze tourism statistics,
            tourist arrivals, popular destinations and revenue
            through interactive visualizations.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ---------------- FEATURE 1 ----------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="feature-box">

            <div class="feature-title">
                📊 Analyze Tourism Statistics
            </div>

            <div class="feature-text">
                Explore domestic and foreign tourist statistics.
            </div>

        </div>
        """, unsafe_allow_html=True)

    # ---------------- FEATURE 2 ----------------

    with col2:

        st.markdown("""
        <div class="feature-box">

            <div class="feature-title">
                📍 Discover Popular Destinations
            </div>

            <div class="feature-text">
                Explore popular tourist destinations.
            </div>

        </div>
        """, unsafe_allow_html=True)

    # ---------------- FEATURE 3 ----------------

    col3, col4 = st.columns(2)

    with col3:

        st.markdown("""
        <div class="feature-box">

            <div class="feature-title">
                📈 Explore Tourist Arrival Trends
            </div>

            <div class="feature-text">
                Analyze tourism growth over time.
            </div>

        </div>
        """, unsafe_allow_html=True)

    # ---------------- FEATURE 4 ----------------

    with col4:

        st.markdown("""
        <div class="feature-box">

            <div class="feature-title">
                💰 Understand Tourism Revenue
            </div>

            <div class="feature-text">
                Study tourism revenue across states and years.
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ---------------- GET STARTED ----------------

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button("🚀 Get Started", use_container_width=True):

            st.session_state.started = True
            st.rerun()

    st.markdown("""
    <div class="footer">
        Tourism Statistics Visualization Portal
    </div>
    """, unsafe_allow_html=True)

    st.stop()


# =========================================================
# LOAD DATA
# =========================================================

try:

    df = pd.read_csv("tourism_data.csv")

except FileNotFoundError:

    st.error("❌ tourism_data.csv file not found.")

    st.info(
        "Make sure tourism_data.csv is inside the same folder as app.py."
    )

    st.stop()


# =========================================================
# REQUIRED COLUMNS
# =========================================================

required_columns = [
    "Year",
    "State",
    "Tourist Place",
    "Domestic Tourists",
    "Foreign Tourists",
    "Revenue",
    "Season",
    "Month",
    "Category",
    "District"
]


missing_columns = [
    col for col in required_columns
    if col not in df.columns
]


if missing_columns:

    st.error("❌ Missing columns in tourism_data.csv:")

    st.write(missing_columns)

    st.stop()


# =========================================================
# DATA CLEANING
# =========================================================

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

df["Domestic Tourists"] = pd.to_numeric(
    df["Domestic Tourists"],
    errors="coerce"
)

df["Foreign Tourists"] = pd.to_numeric(
    df["Foreign Tourists"],
    errors="coerce"
)

df["Revenue"] = pd.to_numeric(
    df["Revenue"],
    errors="coerce"
)

df = df.dropna(
    subset=[
        "Year",
        "Domestic Tourists",
        "Foreign Tourists",
        "Revenue"
    ]
)

df["Year"] = df["Year"].astype(int)

df["Total Tourists"] = (
    df["Domestic Tourists"] +
    df["Foreign Tourists"]
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🌍 Tourism Portal")

page = st.sidebar.selectbox(
    "Navigation",
    [
        "🏠 Home",
        "📊 Tourism Overview",
        "📈 Tourist Trends",
        "📍 Destination Analysis",
        "💰 Revenue Insights"
    ]
)


# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.markdown("---")

st.sidebar.subheader("🔎 Filters")


# Year filter

years = sorted(df["Year"].unique())

selected_year = st.sidebar.selectbox(
    "📅 Select Year",
    ["All"] + years
)


# State filter

states = sorted(df["State"].unique())

selected_state = st.sidebar.selectbox(
    "📍 Select State",
    ["All"] + states
)


# Season filter

seasons = sorted(df["Season"].dropna().unique())

selected_season = st.sidebar.selectbox(
    "🌤️ Select Season",
    ["All"] + seasons
)


# =========================================================
# APPLY FILTERS
# =========================================================

filtered_df = df.copy()


if selected_year != "All":

    filtered_df = filtered_df[
        filtered_df["Year"] == selected_year
    ]


if selected_state != "All":

    filtered_df = filtered_df[
        filtered_df["State"] == selected_state
    ]


if selected_season != "All":

    filtered_df = filtered_df[
        filtered_df["Season"] == selected_season
    ]


# =========================================================
# COMMON VALUES
# =========================================================

total_domestic = filtered_df["Domestic Tourists"].sum()

total_foreign = filtered_df["Foreign Tourists"].sum()

total_tourists = filtered_df["Total Tourists"].sum()

total_revenue = filtered_df["Revenue"].sum()


# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Home":

    st.title("🌍 Tourism Dashboard")

    st.write(
        "Interactive analysis of tourism statistics "
        "across states, destinations and years."
    )

    st.info(
        f"📌 Showing {len(filtered_df)} records"
    )

    # ---------------- KPI CARDS ----------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-title">
                    Domestic Tourists
                </div>

                <div class="kpi-value">
                    {total_domestic:,.0f}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-title">
                    Foreign Tourists
                </div>

                <div class="kpi-value">
                    {total_foreign:,.0f}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-title">
                    Total Tourists
                </div>

                <div class="kpi-value">
                    {total_tourists:,.0f}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-title">
                    Total Revenue
                </div>

                <div class="kpi-value">
                    ₹{total_revenue:,.0f}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # QUICK INSIGHTS
    # =====================================================

    st.subheader("🔍 Quick Insights")

    if not filtered_df.empty:

        highest_arrival_state = (
            filtered_df
            .groupby("State")["Total Tourists"]
            .sum()
            .idxmax()
        )

        popular_destination = (
            filtered_df
            .groupby("Tourist Place")["Total Tourists"]
            .sum()
            .idxmax()
        )

        highest_revenue_state = (
            filtered_df
            .groupby("State")["Revenue"]
            .sum()
            .idxmax()
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                f"""
                <div class="insight-box">
                    <b>Highest Tourist Arrivals</b>
                    <br><br>
                    📍 {highest_arrival_state}
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div class="insight-box">
                    <b>Most Popular Destination</b>
                    <br><br>
                    📍 {popular_destination}
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            st.markdown(
                f"""
                <div class="insight-box">
                    <b>Highest Tourism Revenue</b>
                    <br><br>
                    💰 {highest_revenue_state}
                </div>
                """,
                unsafe_allow_html=True
            )


    # =====================================================
    # CHART 1 - DOMESTIC VS FOREIGN
    # =====================================================

    st.subheader("📊 Tourist Arrivals")

    arrival_data = pd.DataFrame({
        "Type": [
            "Domestic Tourists",
            "Foreign Tourists"
        ],
        "Count": [
            total_domestic,
            total_foreign
        ]
    })

    fig = px.bar(
        arrival_data,
        x="Type",
        y="Count",
        text="Count",
        title="Domestic vs Foreign Tourist Arrivals"
    )

    fig.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # CHART 2 - YEARLY TREND
    # =====================================================

    st.subheader("📈 Tourist Arrival Trend")

    yearly_data = (
        filtered_df
        .groupby("Year", as_index=False)
        .agg({
            "Domestic Tourists": "sum",
            "Foreign Tourists": "sum"
        })
    )

    yearly_data["Total Tourists"] = (
        yearly_data["Domestic Tourists"] +
        yearly_data["Foreign Tourists"]
    )

    fig = px.line(
        yearly_data,
        x="Year",
        y="Total Tourists",
        markers=True,
        title="Year-wise Tourist Arrival Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # CHART 3 - STATE SCATTER
    # =====================================================

    st.subheader("📍 State-wise Tourism Performance")

    state_data = (
        filtered_df
        .groupby("State", as_index=False)
        .agg({
            "Domestic Tourists": "sum",
            "Foreign Tourists": "sum",
            "Revenue": "sum"
        })
    )

    state_data["Total Tourists"] = (
        state_data["Domestic Tourists"] +
        state_data["Foreign Tourists"]
    )

    fig = px.scatter(
        state_data,
        x="Total Tourists",
        y="Revenue",
        size="Total Tourists",
        color="State",
        hover_name="State",
        title="State-wise Tourism Performance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # CHART 4 - REVENUE TREEMAP
    # =====================================================

    st.subheader("💰 Revenue Distribution")

    revenue_data = (
        filtered_df
        .groupby("State", as_index=False)["Revenue"]
        .sum()
    )

    fig = px.treemap(
        revenue_data,
        path=["State"],
        values="Revenue",
        title="State-wise Revenue Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # CHART 5 - POPULAR DESTINATIONS
    # =====================================================

    st.subheader("📍 Popular Tourist Destinations")

    destination_data = (
        filtered_df
        .groupby("Tourist Place", as_index=False)["Total Tourists"]
        .sum()
        .sort_values(
            "Total Tourists",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        destination_data,
        x="Total Tourists",
        y="Tourist Place",
        orientation="h",
        title="Top Tourist Destinations"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# TOURISM OVERVIEW
# =========================================================

elif page == "📊 Tourism Overview":

    st.title("📊 Tourism Overview")

    st.write(
        "Detailed overview of tourism performance "
        "across states, categories and seasons."
    )


    # =====================================================
    # TREEMAP
    # =====================================================

    st.subheader("🌳 State and Category Distribution")

    treemap_data = (
        filtered_df
        .groupby(
            ["State", "Category"],
            as_index=False
        )["Total Tourists"]
        .sum()
    )

    fig = px.treemap(
        treemap_data,
        path=["State", "Category"],
        values="Total Tourists",
        title="Tourism Distribution by State and Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # RADAR CHART
    # =====================================================

    st.subheader("🎯 Tourism Performance Radar")

    radar_data = (
        filtered_df
        .groupby("State", as_index=False)
        .agg({
            "Domestic Tourists": "sum",
            "Foreign Tourists": "sum",
            "Revenue": "sum",
            "Total Tourists": "sum"
        })
    )

    if len(radar_data) >= 1:

        metrics = [
            "Domestic Tourists",
            "Foreign Tourists",
            "Revenue",
            "Total Tourists"
        ]

        max_values = radar_data[metrics].max()

        max_values = max_values.replace(
            0,
            1
        )

        fig = go.Figure()

        for _, row in radar_data.iterrows():

            normalized_values = [
                (row[metric] / max_values[metric]) * 100
                for metric in metrics
            ]

            fig.add_trace(
                go.Scatterpolar(
                    r=normalized_values,
                    theta=metrics,
                    fill="toself",
                    name=row["State"]
                )
            )

        fig.update_layout(
            title="State-wise Tourism Performance",
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # =====================================================
    # CATEGORY DONUT
    # =====================================================

    st.subheader("🍩 Tourism by Category")

    category_data = (
        filtered_df
        .groupby("Category", as_index=False)["Total Tourists"]
        .sum()
    )

    fig = px.pie(
        category_data,
        names="Category",
        values="Total Tourists",
        hole=0.5,
        title="Tourist Distribution by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # POLAR CHART
    # =====================================================

    st.subheader("🌤️ Tourism by Season")

    season_data = (
        filtered_df
        .groupby("Season", as_index=False)["Total Tourists"]
        .sum()
    )

    fig = px.bar_polar(
        season_data,
        r="Total Tourists",
        theta="Season",
        color="Season",
        title="Season-wise Tourist Arrivals"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# TOURIST TRENDS
# =========================================================

elif page == "📈 Tourist Trends":

    st.title("📈 Tourist Trends")

    st.write(
        "Analyse tourist arrivals and seasonal trends over time."
    )


    # =====================================================
    # AREA CHART
    # =====================================================

    st.subheader("📊 Domestic and Foreign Tourist Trend")

    yearly_data = (
        filtered_df
        .groupby("Year", as_index=False)
        .agg({
            "Domestic Tourists": "sum",
            "Foreign Tourists": "sum"
        })
    )

    fig = px.area(
        yearly_data,
        x="Year",
        y=[
            "Domestic Tourists",
            "Foreign Tourists"
        ],
        title="Domestic vs Foreign Tourist Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # TOTAL LINE CHART
    # =====================================================

    yearly_total = (
        filtered_df
        .groupby("Year", as_index=False)["Total Tourists"]
        .sum()
    )

    fig = px.line(
        yearly_total,
        x="Year",
        y="Total Tourists",
        markers=True,
        title="Total Tourist Growth"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # MONTHLY HEATMAP
    # =====================================================

    st.subheader("🔥 Monthly Tourist Heatmap")

    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    heatmap_data = (
        filtered_df
        .groupby(
            ["Year", "Month"],
            as_index=False
        )["Total Tourists"]
        .sum()
    )

    heatmap_pivot = heatmap_data.pivot(
        index="Year",
        columns="Month",
        values="Total Tourists"
    )

    existing_months = [
        month
        for month in month_order
        if month in heatmap_pivot.columns
    ]

    heatmap_pivot = heatmap_pivot[
        existing_months
    ]

    if not heatmap_pivot.empty:

        fig = px.imshow(
            heatmap_pivot,
            aspect="auto",
            title="Year-wise Monthly Tourist Arrivals"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # =====================================================
    # SEASON DONUT
    # =====================================================

    st.subheader("🍩 Tourist Distribution by Season")

    season_data = (
        filtered_df
        .groupby("Season", as_index=False)["Total Tourists"]
        .sum()
    )

    fig = px.pie(
        season_data,
        names="Season",
        values="Total Tourists",
        hole=0.5,
        title="Season-wise Tourist Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# DESTINATION ANALYSIS
# =========================================================

elif page == "📍 Destination Analysis":

    st.title("📍 Destination Analysis")

    st.write(
        "Analyse tourist destinations, districts and categories."
    )


    # =====================================================
    # BUBBLE CHART
    # =====================================================

    st.subheader("🫧 Tourist Arrivals vs Revenue")

    destination_data = (
        filtered_df
        .groupby("Tourist Place", as_index=False)
        .agg({
            "Total Tourists": "sum",
            "Revenue": "sum"
        })
    )

    fig = px.scatter(
        destination_data,
        x="Total Tourists",
        y="Revenue",
        size="Total Tourists",
        color="Tourist Place",
        hover_name="Tourist Place",
        title="Destination-wise Tourist Arrivals vs Revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # DESTINATION TREEMAP
    # =====================================================

    st.subheader("🌳 Destination Revenue Distribution")

    destination_revenue = (
        filtered_df
        .groupby(
            ["State", "Tourist Place"],
            as_index=False
        )["Revenue"]
        .sum()
    )

    fig = px.treemap(
        destination_revenue,
        path=[
            "State",
            "Tourist Place"
        ],
        values="Revenue",
        title="Revenue by State and Destination"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # SUNBURST
    # =====================================================

    st.subheader("☀️ State → Category → Destination")

    sunburst_data = (
        filtered_df
        .groupby(
            [
                "State",
                "Category",
                "Tourist Place"
            ],
            as_index=False
        )["Total Tourists"]
        .sum()
    )

    fig = px.sunburst(
        sunburst_data,
        path=[
            "State",
            "Category",
            "Tourist Place"
        ],
        values="Total Tourists",
        title="Tourism Hierarchy"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # DISTRICT BAR
    # =====================================================

    st.subheader("📊 District-wise Domestic Arrivals")

    district_data = (
        filtered_df
        .groupby("District", as_index=False)["Domestic Tourists"]
        .sum()
        .sort_values(
            "Domestic Tourists",
            ascending=False
        )
    )

    fig = px.bar(
        district_data,
        x="Domestic Tourists",
        y="District",
        orientation="h",
        title="District-wise Domestic Tourist Arrivals"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# REVENUE INSIGHTS
# =========================================================

elif page == "💰 Revenue Insights":

    st.title("💰 Revenue Insights")

    st.write(
        "Analyse tourism revenue across years, states "
        "and destinations."
    )


    # =====================================================
    # REVENUE KPI
    # =====================================================

    revenue_average = (
        filtered_df["Revenue"].mean()
        if not filtered_df.empty
        else 0
    )

    highest_revenue = (
        filtered_df["Revenue"].max()
        if not filtered_df.empty
        else 0
    )


    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-title">
                    Total Revenue
                </div>

                <div class="kpi-value">
                    ₹{total_revenue:,.0f}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-title">
                    Average Revenue
                </div>

                <div class="kpi-value">
                    ₹{revenue_average:,.0f}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-title">
                    Highest Revenue Record
                </div>

                <div class="kpi-value">
                    ₹{highest_revenue:,.0f}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # YEARLY REVENUE
    # =====================================================

    st.subheader("📈 Year-wise Revenue")

    yearly_revenue = (
        filtered_df
        .groupby("Year", as_index=False)["Revenue"]
        .sum()
        .sort_values("Year")
    )

    fig = px.area(
        yearly_revenue,
        x="Year",
        y="Revenue",
        markers=True,
        title="Year-wise Tourism Revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # WATERFALL CHART
    # =====================================================

    st.subheader("💧 Revenue Change Waterfall")

    if len(yearly_revenue) >= 2:

        years_list = yearly_revenue["Year"].tolist()

        revenue_values = yearly_revenue["Revenue"].tolist()

        measures = ["absolute"]

        values = [revenue_values[0]]

        labels = [str(years_list[0])]

        for i in range(1, len(revenue_values)):

            change = (
                revenue_values[i]
                - revenue_values[i - 1]
            )

            measures.append("relative")

            values.append(change)

            labels.append(
                f"{years_list[i]} Change"
            )

        measures.append("total")

        values.append(revenue_values[-1])

        labels.append("Final Revenue")

        fig = go.Figure(
            go.Waterfall(
                x=labels,
                y=values,
                measure=measures,
                connector={
                    "line": {
                        "dash": "dot"
                    }
                }
            )
        )

        fig.update_layout(
            title="Year-wise Revenue Increase / Decrease",
            yaxis_title="Revenue"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "💡 Select 'All' for Year to view the Waterfall Chart."
        )


    # =====================================================
    # STATE REVENUE TREEMAP
    # =====================================================

    st.subheader("🌳 State-wise Revenue")

    state_revenue = (
        filtered_df
        .groupby("State", as_index=False)["Revenue"]
        .sum()
    )

    fig = px.treemap(
        state_revenue,
        path=["State"],
        values="Revenue",
        title="Revenue Distribution by State"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # CATEGORY REVENUE DONUT
    # =====================================================

    st.subheader("🍩 Category-wise Revenue")

    category_revenue = (
        filtered_df
        .groupby("Category", as_index=False)["Revenue"]
        .sum()
    )

    fig = px.pie(
        category_revenue,
        names="Category",
        values="Revenue",
        hole=0.5,
        title="Revenue by Tourism Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # TOP REVENUE DESTINATIONS
    # =====================================================

    st.subheader("💰 Top Revenue Destinations")

    top_destinations = (
        filtered_df
        .groupby("Tourist Place", as_index=False)["Revenue"]
        .sum()
        .sort_values(
            "Revenue",
            ascending=False
        )
        .head(10)
    )

    fig = px.scatter(
        top_destinations,
        x="Tourist Place",
        y="Revenue",
        size="Revenue",
        color="Tourist Place",
        title="Top Revenue Generating Destinations"
    )

    fig.update_layout(
        xaxis_tickangle=-45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    🌍 Tourism Statistics Visualization Portal
    <br>
    Developed using Python, Streamlit, Pandas and Plotly

</div>
""", unsafe_allow_html=True)