import requests
import streamlit as st

from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.title(":blue[Autism Spectrum Disorder]")
st.write("---")
with st.container():
    col1,col2= st.columns([3,2])
    with col1:
        st.title("What is Autism Spectrum Disorder?")
        st.write("""
        Autism spectrum disorder (ASD) is a developmental disability caused by differences in the brain. People with ASD often have problems with social communication and interaction, and restricted or repetitive behaviors or interests. People with ASD may also have different ways of learning, moving, or paying attention.
        """)
    with col2:
        img1=Image.open("image/asd_child.jpg")
        st.image(img1,width=300)


with st.container():
    col1,col2= st.columns([4,2])
    with col1:
        st.title("What Causes Autism Spectrum Disorder?")
        st.write("""
        The Autism Spectrum Disorder Foundation lists the following as possible causes of ASD:

        :blue[Genetics] : Research suggests that ASD can be caused by a combination of genetic and environmental factors. Some genes have been identified as being associated with an increased risk for ASD, but no single gene has been proven to cause ASD.
        
        :blue[Environmental factors] : Studies are currently underway to explore whether certain exposure to toxins during pregnancy or after birth can increase the risk for developing ASD.
        
        :blue[Brain differences] : Differences in certain areas of the brain have been observed in people with ASD, compared to those without ASD. It is not yet known what causes these differences.
        """)
    with col2:
        img1=Image.open("image/causes-of-autism.png")
        st.image(img1,width=350, caption="Causes of ASD")


with st.container():
    col1,col2= st.columns([4,2])
    with col1:
        st.title("Symptoms of ASD:")
    
        st.write("""
        1. Avoids or does not keep eye contact
        2. Does not respond to name by 9 months of age
        3. Does not show facial expressions like happy, sad, angry, and surprised by 9 months of age
        4. Lines up toys or other objects and gets upset when order is changed
        5. Repeats words or phrases over and over (called echolalia)
        6. Plays with toys the same way every time
        7. Delayed language skills
        8. Delayed movement skills
        9. Delayed cognitive or learning skills
        10. Hyperactive, impulsive, and/or inattentive behavior
        11. Epilepsy or seizure disorder
        12. Unusual eating and sleeping habits
        13. Gastrointestinal issues (for example, constipation)
        14. Unusual mood or emotional reactions
        15. Anxiety, stress, or excessive worry
        16. Lack of fear or more fear than expected, etc.
        """)
        st.write("[Learn More >](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders)")
    with col2:
        img=Image.open("image/autism.png")
        st.image(img,caption="Signs of ASD")
        img1=Image.open("image/Strategies.jpeg")
        st.image(img1,caption="")
    


# ---- WHAT I DO ----
with st.container():

    left_column, right_column = st.columns([4,2])
    with left_column:
        st.title("Relevent statistics ")
        
        st.write("""
            The exact prevalence of Autism Spectrum Disorder (ASD) in India is not well-established due to a lack of nationwide studies and consistent diagnostic criteria. However, some studies have estimated that the prevalence of ASD in India is between 1 and 2 per 1000 children.
            A recent study published in the Indian Journal of Pediatrics in 2020 estimated the prevalence of ASD in children aged 2 to 9 years in Kolkata, India, to be 1.25%. Another study published in the Journal of Autism and Developmental Disorders in 2018 found a prevalence of 0.64% among school-aged children in Chennai, India.
            
            • Prevalance of Autism: Between 1 in 500 (2/1,000) to 1 in 166 children (6/1,000) have an Autism Spectrum Disorder (Center for Disease Control).
            
            • Prevalance Rate: Approx. 1 in 500 or 0.20% or more than 2,160,000 people in India.
            
            • Incidence Rate: Approx. 1 in 90,666 or 11,914 people in India.
            
            • Incidence extrapolations for India for Autism: 11,914 per year, 250 per month, 57 per week, 8 per day, 1.4 per hour.
            
            • Autism is four times more prevalent in boys than girls in the US (Autism Society of America).
            
            • Autism is more common than Down Syndrome, which occurs in 1 out of 800 births.
            
            • The rate of incidence of autism is increasing 10-17% per year in the US (Autism Society of America).
            
            • Prevalence of autism is expected to reach 4 million people in the next decade in the US (Autism Society of America).
            """)

    with right_column:
        img=Image.open("image/autism-stats-1.jpg")
        st.image(img,width=350,caption="ASD ststistics")
        img1=Image.open("image/autism-stats-2.png")
        st.image(img1,width=350,caption="USA data over 18 years")

with st.container():
    st.title("World Autism Awareness Day")
    st.write(
        "This year, WAAD will be observed with a virtual event on Sunday, 2 April, from 10:00 a.m. to 1:00 p.m. EDT.The event is organized in close collaboration with autistic people and will feature autistic people from around the world discussing how the transformation in the narrative around neurodiversity can continue to be furthered in order to overcome barriers and improve the lives of autistic people. It will also address the contributions that autistic people make – and can make – to society, and to the achievement of the Sustainable Development Goals."
    )
c1,c2=st.columns([5,5])
im=Image.open("image/World.png")
c1.image(im,caption="")
im1=Image.open("image/Worlds.png")
   
c2.image(im1,caption="")
        