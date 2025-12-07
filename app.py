import streamlit as st
from src.helper import ask_ollama,extract_text_from_pdf
from src.job_api import fetch_linkedin_jobs,fetch_naukri_jobs

st.set_page_config(page_title="Job Recommendation System", page_icon=":tada:", layout="wide")
st.title("Job Recommendation System")

st.markdown("Upload your resume and let the system recommend jobs for you.")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

if uploaded_file:
    with st.spinner("Processing resume..."):
        resumetext = extract_text_from_pdf(uploaded_file)

    if not resumetext or len(resumetext.strip()) < 20:
        st.error("Unable to extract text from the PDF. Please upload a proper resume.")
        st.stop()

    # ---------------- SUMMARY ----------------
    with st.spinner("Summarizing resume..."):
        summary = ask_ollama(
            f"Summarize this resume highlighting the skills, education and experience:\n\n{resumetext}",
            max_tokens=1000
        )

    # ---------------- SKILL GAPS ----------------
    with st.spinner("Detecting skill gaps..."):
        skillgap = ask_ollama(
            f"Analyze this resume and list missing skills, certifications and experience required:\n\n{resumetext}",
            max_tokens=1000
        )

    # ---------------- ROADMAP ----------------
    with st.spinner("Generating future roadmap..."):
        roadmap = ask_ollama(
            f"Analyze this resume and suggest a future career roadmap (skills, certifications, experience):\n\n{resumetext}",
            max_tokens=1000
        )

    # ---------------- DISPLAY OUTPUT ----------------
    st.markdown("---")
    st.header("Resume Summary")
    st.markdown(f"<div style='background:#f5f5f5;padding:10px;border-radius:5px'>{summary}</div>",
                unsafe_allow_html=True)

    st.markdown("---")
    st.header("Skill Gaps")
    st.markdown(f"<div style='background:#f5f5f5;padding:10px;border-radius:5px'>{skillgap}</div>",
                unsafe_allow_html=True)

    st.markdown("---")
    st.header("Future Roadmap")
    st.markdown(f"<div style='background:#f5f5f5;padding:10px;border-radius:5px'>{roadmap}</div>",
                unsafe_allow_html=True)

    st.success("Resume analysis completed successfully!")

    # ---------------- JOB RECOMMENDATION ----------------
    if st.button("Get Job Recommendations"):
        with st.spinner("Generating keywords..."):
            keywords = ask_ollama(
                f"Based on the resume summary, suggest the best job titles and keywords for job search. "
                f"Return a comma-separated list with no explanation:\n\n{summary}",
                max_tokens=300
            )
            search_keywords_clean = keywords.replace("\n", "").strip()

        st.success(f"Job keywords: {search_keywords_clean}")

        with st.spinner("Fetching jobs..."):
            linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, rows=60)
            naukri_jobs = fetch_naukri_jobs(search_keywords_clean, rows=60)

        st.success("Jobs fetched successfully!")

        # -------- LinkedIn Jobs --------
        st.markdown("---")
        st.header("LinkedIn Jobs")

        if linkedin_jobs:
            for job in linkedin_jobs:
                st.markdown(f"### {job['title']}")
                st.markdown(f"**{job['company']}** — {job['location']}")
                st.markdown(job['description'])
                st.markdown(f"[Apply Here]({job['url']})")
                st.markdown("---")
        else:
            st.warning("No jobs found on LinkedIn")

        # -------- Naukri Jobs --------
        st.markdown("---")
        st.header("Naukri Jobs")

        if naukri_jobs:
            for job in naukri_jobs:
                st.markdown(f"### {job['title']}")
                st.markdown(f"**{job['company']}** — {job['location']}")
                st.markdown(job['description'])
                st.markdown(f"[Apply Here]({job['url']})")
                st.markdown("---")
        else:
            st.warning("No jobs found on Naukri")