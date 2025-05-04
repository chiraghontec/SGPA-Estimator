# GPA Estimator Streamlit Version with Target Marks Prediction
import streamlit as st

def main():
    st.title("📊 SGPA Estimator - REVA University")
    st.markdown("Estimate your SGPA based on IA and SEE marks or predict required marks to reach your target SGPA.")

    num_subjects = st.number_input("Enter number of subjects (Theory + Lab):", min_value=1, step=1)
    target_gpa = st.number_input("Enter your target SGPA:", min_value=0.0, max_value=10.0, step=0.1)

    subject_data = []

    for i in range(num_subjects):
        st.subheader(f"Subject {i+1}")
        name = st.text_input(f"Subject name {i+1}", key=f"name_{i}")
        subject_type = st.selectbox(f"Type (Theory/Lab) {i+1}", options=["Theory", "Lab"], key=f"type_{i}")
        credits = st.number_input(f"Credits for {name}", min_value=1, step=1, key=f"credits_{i}")

        ia1 = st.number_input(f"IA-1 + Assignment marks (out of 50) for {name}", min_value=0.0, max_value=50.0, step=0.5, key=f"ia1_{i}")
        ia2 = st.number_input(f"IA-2 + Assignment marks (out of 50) for {name} (Leave 0 if not yet done)", min_value=0.0, max_value=50.0, step=0.5, key=f"ia2_{i}")
        see = st.number_input(f"SEE marks (out of 100) for {name} (Leave 0 if not yet written)", min_value=0.0, max_value=100.0, step=0.5, key=f"see_{i}")

        subject_data.append({
            "name": name,
            "type": subject_type,
            "credits": credits,
            "ia1": ia1,
            "ia2": ia2,
            "see": see
        })

    if st.button("Calculate SGPA and Analyze"):
        total_score = 0
        total_credits = 0

        st.subheader("📋 Results")
        for subj in subject_data:
            name = subj["name"]
            st.markdown(f"**{name}**")

            if subj["type"] == "Theory":
                internal = ((subj["ia1"] + subj["ia2"]) / 100) * 50
                external = (subj["see"] / 100) * 50
                final_score = internal + external

            elif subj["type"] == "Lab":
                internal = subj["ia1"] + subj["ia2"]
                external = (subj["see"] / 100) * 65
                final_score = ((internal + external) / 135) * 100
            else:
                continue

            total_score += final_score * subj["credits"]
            total_credits += subj["credits"]

            st.write(f"Final Score: {final_score:.2f} / 100")

        sgpa = total_score / total_credits if total_credits != 0 else 0
        st.success(f"🎓 Estimated SGPA: {sgpa:.2f}")

        if sgpa >= target_gpa:
            st.info("🎯 You are on track to reach your target SGPA!")
        else:
            st.warning("⚠️ You need to improve to reach your target SGPA. Check required scores below:")

            st.subheader("📈 Estimated Required Marks")
            total_target_score = target_gpa * total_credits
            for subj in subject_data:
                name = subj["name"]
                st.markdown(f"**{name}**")
                credit = subj["credits"]
                required_score = (total_target_score - (total_score - subj["credits"] * ((subj["ia1"] + subj["ia2"] + subj["see"]) if subj["type"] == "Lab" else ((subj["ia1"] + subj["ia2"]) / 100 * 50 + (subj["see"] / 100 * 50)))) / credit)
                if subj["type"] == "Theory":
                    remaining_internal = 50 - (subj["ia1"] + subj["ia2"])
                    remaining_see = 100 - subj["see"]
                    st.write(f"Target final score: {required_score:.2f} / 100")
                    if subj["ia2"] == 0 and subj["see"] == 0:
                        st.write("Try to get higher marks in IA-2 and SEE to compensate.")
                elif subj["type"] == "Lab":
                    st.write(f"Target scaled final score: {required_score:.2f} / 100")

if __name__ == "__main__":
    main()