import streamlit as st
from google import genai
from pydantic import BaseModel
from typing import List, Optional, Dict
import json

# Define Pydantic models for structured outputs
class UIComponent(BaseModel):
    component_type: str
    properties: dict
    description: str

class UIPromptSuggestion(BaseModel):
    prompt_title: str
    suggested_prompt: str
    key_elements: List[str]
    example_output: Optional[str] = None
    prompt_type: str  # 'high-level' or 'detailed'

class UIDesignIdea(BaseModel):
    app_name: str
    description: str
    main_features: List[str]
    target_audience: str
    ui_components: List[str]

class StitchPromptExample(BaseModel):
    category: str
    title: str
    example_prompt: str
    description: str

# Initialize Streamlit page config
st.set_page_config(
    page_title="Stitch UI Prompt Builder",
    page_icon="🎨",
    layout="wide"
)

# Initialize session state
if 'generated_prompts' not in st.session_state:
    st.session_state.generated_prompts = []
if 'prompt_level' not in st.session_state:
    st.session_state.prompt_level = 'high-level'

# App header
st.title("🎨 Stitch UI Prompt Generator")
st.markdown("Generate effective prompts for building user interfaces with Stitch AI")

# Sidebar for API configuration
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Google Gemini API Key", type="password")
    
    if api_key:
        st.success("API Key configured ✓")
        client = genai.Client(api_key=api_key)
    else:
        st.warning("Please enter your Google Gemini API Key")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("This app helps you create effective prompts for Stitch AI following official guidelines.")
    st.markdown("Based on the [Stitch Prompt Guide](https://stitch.ai)")

# Main content area
if api_key:
    # Tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 Stitch Guide", "💡 Sample Ideas", "✨ Generate Prompt", "🎯 Refine Screen", "📝 Saved Prompts"])
    
    with tab1:
        st.header("📚 Stitch Prompt Guide")
        
        guide_col1, guide_col2 = st.columns([1, 1])
        
        with guide_col1:
            st.subheader("1. Starting Your Project")
            
            with st.expander("High-Level vs. Detailed Prompts", expanded=True):
                st.markdown("**High-Level (for brainstorming):**")
                st.code('"An app for marathon runners."', language="text")
                
                st.markdown("**Detailed (for specific results):**")
                st.code('"An app for marathon runners to engage with a community, find partners, get training advice, and find races near them."', language="text")
            
            with st.expander("Set the Vibe with Adjectives"):
                st.markdown("Use adjectives to define the app's feel:")
                st.code('"A vibrant and encouraging fitness tracking app."', language="text")
                st.code('"A minimalist and focused app for meditation."', language="text")
            
            st.subheader("2. Refining Your App")
            
            with st.expander("Be Specific with Changes"):
                st.markdown("Focus on one screen/component with clear instructions:")
                st.code('"On the homepage, add a search bar to the header."', language="text")
                st.code('"Change the primary call-to-action button on the login screen to be larger and use the brand\'s primary blue color."', language="text")
            
            with st.expander("Focus on Specific Screens"):
                st.markdown("**E-commerce Example:**")
                st.code('"Product detail page for a Japandi-styled tea store. Sells herbal teas, ceramics. Neutral, minimal colors, black buttons. Soft, elegant font."', language="text")
        
        with guide_col2:
            st.subheader("3. Controlling App Theme")
            
            with st.expander("Colors"):
                st.markdown("**Specific Color:**")
                st.code('"Change primary color to forest green."', language="text")
                
                st.markdown("**Mood-Based:**")
                st.code('"Update theme to a warm, inviting color palette."', language="text")
            
            with st.expander("Fonts & Borders"):
                st.markdown("**Font Styles:**")
                st.code('"Use a playful sans-serif font."', language="text")
                
                st.markdown("**Button/Border Styles:**")
                st.code('"Make all buttons have fully rounded corners."', language="text")
            
            st.subheader("4. Modifying Images")
            
            with st.expander("Image Guidelines"):
                st.markdown("**General Images:**")
                st.code('"Change background of all product images on landing page to light taupe."', language="text")
                
                st.markdown("**Specific Image:**")
                st.code('"On \'Team\' page, image of \'Dr. Carter\': update her lab coat to black."', language="text")
            
            st.subheader("💡 Pro Tips")
            
            with st.expander("Best Practices", expanded=True):
                tips = [
                    "Be Clear & Concise: Avoid ambiguity",
                    "One Major Change at a Time: Easier to see impact",
                    "Use UI/UX Keywords: navigation bar, CTA button, card layout",
                    "Reference Elements Specifically: 'primary button on sign-up form'",
                    "Iterate & Experiment: Refine with further prompts"
                ]
                for tip in tips:
                    st.markdown(f"• {tip}")
    
    with tab2:
        st.header("Sample UI Building Ideas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Pre-built Templates")
            
            templates = {
                "Dashboard App": {
                    "description": "Analytics dashboard with charts and metrics",
                    "features": ["Real-time data visualization", "Customizable widgets", "Export functionality"],
                    "components": ["Charts", "Cards", "Tables", "Filters"]
                },
                "E-commerce Platform": {
                    "description": "Online shopping interface with product catalog",
                    "features": ["Product search", "Shopping cart", "User reviews", "Payment integration"],
                    "components": ["Product cards", "Search bar", "Cart drawer", "Checkout form"]
                },
                "Social Media Feed": {
                    "description": "Social platform with posts and interactions",
                    "features": ["Post creation", "Like/comment system", "User profiles", "Real-time updates"],
                    "components": ["Post cards", "Comment sections", "User avatars", "Navigation bar"]
                },
                "Task Management": {
                    "description": "Project and task tracking application",
                    "features": ["Task creation", "Kanban boards", "Due dates", "Team collaboration"],
                    "components": ["Task cards", "Drag-drop lists", "Calendar view", "Progress bars"]
                }
            }
            
            selected_template = st.selectbox("Choose a template:", list(templates.keys()))
            
            if selected_template:
                template = templates[selected_template]
                st.info(f"**Description:** {template['description']}")
                st.write("**Key Features:**")
                for feature in template['features']:
                    st.write(f"• {feature}")
                st.write("**UI Components:**")
                for component in template['components']:
                    st.write(f"• {component}")
        
        with col2:
            st.subheader("Generate Custom Ideas")
            
            if st.button("🎲 Generate Random UI Ideas"):
                with st.spinner("Generating ideas..."):
                    try:
                        response = client.models.generate_content(
                            model="gemini-2.0-flash-exp",
                            contents="Generate 3 creative and unique UI application ideas with descriptions, features, and required components. Focus on modern, user-friendly designs. Include adjectives that set the vibe for each app.",
                            config={
                                "response_mime_type": "application/json",
                                "response_schema": list[UIDesignIdea],
                            },
                        )
                        
                        ideas = response.parsed
                        
                        for idx, idea in enumerate(ideas):
                            with st.expander(f"{idea.app_name}", expanded=idx==0):
                                st.write(f"**Description:** {idea.description}")
                                st.write(f"**Target Audience:** {idea.target_audience}")
                                st.write("**Main Features:**")
                                for feature in idea.main_features:
                                    st.write(f"• {feature}")
                                st.write("**UI Components:**")
                                for component in idea.ui_components:
                                    st.write(f"• {component}")
                    
                    except Exception as e:
                        st.error(f"Error generating ideas: {str(e)}")
    
    with tab3:
        st.header("Generate UI Building Prompt")
        
        # Prompt level selector
        prompt_level = st.radio(
            "Choose prompt level:",
            ["high-level", "detailed"],
            format_func=lambda x: "High-Level (Brainstorming)" if x == "high-level" else "Detailed (Specific Results)",
            horizontal=True
        )
        st.session_state.prompt_level = prompt_level
        
        # Input section
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Describe Your UI Project")
            
            if prompt_level == "high-level":
                project_type = st.text_input("What type of app are you building?", 
                                           placeholder="e.g., An app for marathon runners")
                
                vibe_adjectives = st.text_input("Describe the vibe with adjectives:",
                                              placeholder="e.g., vibrant, encouraging, minimalist, focused")
            else:
                project_type = st.text_input("What type of UI are you building?", 
                                           placeholder="e.g., Dashboard, Mobile app, Landing page")
                
                project_description = st.text_area("Describe your project in detail:",
                                                 placeholder="Include the purpose, target users, and key functionality...",
                                                 height=150)
                
                key_features = st.text_area("List key features (one per line):",
                                           placeholder="User authentication\nData visualization\nReal-time updates",
                                           height=100)
                
                vibe_adjectives = st.text_input("Describe the vibe with adjectives:",
                                              placeholder="e.g., vibrant, professional, minimal, playful")
            
            design_style = st.selectbox("Visual style reference:",
                                      ["Japandi (minimal, neutral)", "Corporate and Professional", 
                                       "Vibrant and Playful", "Dark and Elegant", "Custom"])
            
            if design_style == "Custom":
                custom_style = st.text_input("Describe your custom style:")
        
        with col2:
            st.subheader("Theme Options")
            
            # Color options
            color_choice = st.radio("Color specification:", ["Mood-based", "Specific colors"])
            if color_choice == "Specific colors":
                primary_color = st.text_input("Primary color:", placeholder="e.g., forest green, #2ECC71")
            else:
                color_mood = st.text_input("Color mood:", placeholder="e.g., warm and inviting")
            
            # Font options
            font_style = st.selectbox("Font style:",
                                    ["Default", "Playful sans-serif", "Professional serif", 
                                     "Modern sans-serif", "Elegant serif", "Custom"])
            
            if font_style == "Custom":
                custom_font = st.text_input("Describe font style:")
            
            # Component styling
            button_style = st.selectbox("Button style:",
                                      ["Default", "Fully rounded corners", "Sharp corners", 
                                       "Slightly rounded", "Pill-shaped"])
            
            if prompt_level == "detailed":
                st.subheader("Specific Screens")
                specific_screen = st.text_input("Focus on specific screen (optional):",
                                              placeholder="e.g., Product detail page, Login screen")
        
        # Generate prompt button
        if st.button("🚀 Generate Stitch Prompts", type="primary", use_container_width=True):
            if project_type and (prompt_level == "high-level" or project_description):
                with st.spinner("Generating optimized prompt..."):
                    try:
                        # Prepare context for prompt generation based on level
                        if prompt_level == "high-level":
                            context = f"""
                            Prompt Level: High-Level (for brainstorming)
                            App Type: {project_type}
                            Vibe/Adjectives: {vibe_adjectives if 'vibe_adjectives' in locals() else ''}
                            Visual Style: {design_style if design_style != 'Custom' else custom_style if 'custom_style' in locals() else ''}
                            """
                        else:
                            context = f"""
                            Prompt Level: Detailed (for specific results)
                            Project Type: {project_type}
                            Description: {project_description}
                            Features: {key_features}
                            Vibe/Adjectives: {vibe_adjectives if 'vibe_adjectives' in locals() else ''}
                            Visual Style: {design_style if design_style != 'Custom' else custom_style if 'custom_style' in locals() else ''}
                            Color: {primary_color if color_choice == 'Specific colors' and 'primary_color' in locals() else color_mood if 'color_mood' in locals() else ''}
                            Font Style: {font_style if font_style != 'Custom' else custom_font if 'custom_font' in locals() else ''}
                            Button Style: {button_style}
                            Specific Screen: {specific_screen if 'specific_screen' in locals() else ''}
                            """
                        
                        response = client.models.generate_content(
                            model="gemini-2.0-flash-exp",
                            contents=f"""Create 3 different effective Stitch prompts following the official Stitch prompt guidelines.
                            Each prompt should follow Stitch best practices:
                            - Use clear, specific language
                            - Include adjectives to set the vibe
                            - Be concise but descriptive
                            - Follow the appropriate format for {prompt_level} prompts
                            
                            Context: {context}
                            
                            For high-level prompts: Keep them short and conceptual with vibe-setting adjectives.
                            For detailed prompts: Include specific features, components, and styling details.
                            
                            Each prompt should be ready to use directly in Stitch.""",
                            config={
                                "response_mime_type": "application/json",
                                "response_schema": list[UIPromptSuggestion],
                            },
                        )
                        
                        suggestions = response.parsed
                        
                        st.success("✅ Stitch prompts generated successfully!")
                        
                        for idx, suggestion in enumerate(suggestions):
                            with st.expander(f"Prompt Option {idx + 1}: {suggestion.prompt_title}", expanded=idx==0):
                                st.subheader("Generated Stitch Prompt:")
                                st.info("Click inside the box below and press Ctrl+A to select all, then Ctrl+C to copy")
                                st.code(suggestion.suggested_prompt, language="text")
                                
                                st.subheader("Key Elements Covered:")
                                for element in suggestion.key_elements:
                                    st.write(f"✓ {element}")
                                
                                # Three buttons in a clean row
                                col1, col2, col3 = st.columns(3)
                                with col1:
                                    st.download_button(
                                        label="📥 Download Prompt",
                                        data=suggestion.suggested_prompt,
                                        file_name=f"stitch_prompt_{idx + 1}.txt",
                                        mime="text/plain",
                                        key=f"download_{idx}",
                                        use_container_width=True
                                    )
                                
                                with col2:
                                    if st.button(f"💾 Save Prompt", key=f"save_{idx}", use_container_width=True):
                                        st.session_state.generated_prompts.append({
                                            "title": suggestion.prompt_title,
                                            "prompt": suggestion.suggested_prompt,
                                            "project_type": project_type,
                                            "level": prompt_level,
                                            "timestamp": "Just now"
                                        })
                                        st.toast("Prompt saved!", icon="✅")
                                
                                with col3:
                                    if st.button(f"🎯 Use for Refinement", key=f"refine_{idx}", use_container_width=True):
                                        st.session_state.base_prompt = suggestion.suggested_prompt
                                        st.toast("Prompt set for refinement!", icon="🎯")
                    
                    except Exception as e:
                        st.error(f"Error generating prompts: {str(e)}")
            else:
                if prompt_level == "high-level":
                    st.warning("Please fill in the app type field.")
                else:
                    st.warning("Please fill in the project type and description fields.")
    
    with tab4:
        st.header("🎯 Refine Screen by Screen")
        
        st.markdown("Use this section to make specific, incremental changes to your app screens.")
        
        # Base prompt input
        if 'base_prompt' in st.session_state:
            base_prompt = st.text_area("Base app description:", 
                                     value=st.session_state.base_prompt,
                                     height=100)
        else:
            base_prompt = st.text_area("Base app description:", 
                                     placeholder="Paste your initial app prompt here or select from saved prompts",
                                     height=100)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Specify Your Change")
            
            # Screen selection
            screen_name = st.text_input("Which screen to modify?",
                                      placeholder="e.g., homepage, login screen, product detail page")
            
            # Change type
            change_type = st.selectbox("Type of change:",
                                     ["Add component", "Modify component", "Change styling", 
                                      "Update images", "Adjust layout", "Change text/language"])
            
            # Specific change description
            if change_type == "Add component":
                change_detail = st.text_area("What to add:",
                                           placeholder="e.g., Add a search bar to the header",
                                           height=80)
            elif change_type == "Modify component":
                change_detail = st.text_area("What to modify:",
                                           placeholder="e.g., Make the primary CTA button larger and blue",
                                           height=80)
            elif change_type == "Change styling":
                style_element = st.selectbox("Style element:",
                                           ["Colors", "Fonts", "Borders/Corners", "Spacing", "Overall theme"])
                change_detail = st.text_area("Style change:",
                                           placeholder="e.g., Change primary color to forest green",
                                           height=80)
            elif change_type == "Update images":
                image_target = st.radio("Image scope:", ["Specific image", "All images on screen", "Background images"])
                change_detail = st.text_area("Image change:",
                                           placeholder="e.g., Change background of all product images to light taupe",
                                           height=80)
            elif change_type == "Adjust layout":
                change_detail = st.text_area("Layout adjustment:",
                                           placeholder="e.g., Switch to a 3-column grid for product cards",
                                           height=80)
            else:  # Change text/language
                change_detail = st.text_area("Text/language change:",
                                           placeholder="e.g., Switch all button text to Spanish",
                                           height=80)
        
        with col2:
            st.subheader("Quick Templates")
            
            refinement_templates = {
                "Add search": "On the {screen}, add a search bar to the header.",
                "Enlarge CTA": "Change the primary call-to-action button on the {screen} to be larger and use the brand's primary color.",
                "Round buttons": "Make all buttons have fully rounded corners.",
                "Update theme": "Update theme to a {mood} color palette.",
                "Change font": "Use a {style} font for all text.",
                "Add spacing": "Increase spacing between all components for better readability.",
                "Mobile optimize": "Optimize the {screen} layout for mobile devices."
            }
            
            template_choice = st.selectbox("Use a template:", 
                                         ["None"] + list(refinement_templates.keys()))
            
            if template_choice != "None":
                template = refinement_templates[template_choice]
                st.info(f"Template: {template}")
        
        # Generate refinement prompt
        if st.button("🔧 Generate Refinement Prompt", type="primary", use_container_width=True):
            if base_prompt and screen_name and change_detail:
                with st.spinner("Generating refinement prompt..."):
                    try:
                        refinement_context = f"""
                        Base App: {base_prompt}
                        Screen to Modify: {screen_name}
                        Change Type: {change_type}
                        Specific Change: {change_detail}
                        """
                        
                        response = client.models.generate_content(
                            model="gemini-2.0-flash-exp",
                            contents=f"""Create a specific, clear Stitch refinement prompt following best practices.
                            The prompt should:
                            - Be specific about what to change and how
                            - Reference the specific screen/component
                            - Use clear UI/UX terminology
                            - Be concise but complete
                            - Follow Stitch's guideline of one major change at a time
                            
                            Context: {refinement_context}
                            
                            Generate just the refinement prompt text, nothing else.""",
                        )
                        
                        refinement_prompt = response.text.strip()
                        
                        st.success("✅ Refinement prompt generated!")
                        st.subheader("Your Refinement Prompt:")
                        st.info("Click inside the box below and press Ctrl+A to select all, then Ctrl+C to copy")
                        st.code(refinement_prompt, language="text")
                        
                        # Three buttons in a clean row
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.download_button(
                                label="📥 Download Refinement",
                                data=refinement_prompt,
                                file_name="stitch_refinement.txt",
                                mime="text/plain",
                                use_container_width=True
                            )
                        
                        with col2:
                            if st.button("💾 Save to History", use_container_width=True):
                                st.session_state.generated_prompts.append({
                                    "title": f"Refinement: {change_type} on {screen_name}",
                                    "prompt": refinement_prompt,
                                    "project_type": "Screen Refinement",
                                    "level": "refinement",
                                    "timestamp": "Just now"
                                })
                                st.toast("Refinement saved!", icon="✅")
                        
                        with col3:
                            if st.button("🎯 Use for Next Refinement", use_container_width=True):
                                st.session_state.base_prompt = refinement_prompt
                                st.toast("Refinement loaded as base!", icon="🎯")
                    
                    except Exception as e:
                        st.error(f"Error generating refinement: {str(e)}")
            else:
                st.warning("Please fill in all required fields: base app description, screen name, and change details.")
    
    with tab5:
        st.header("📝 Saved Prompts")
        
        if st.session_state.generated_prompts:
            # Filter options
            filter_type = st.selectbox("Filter by type:", 
                                     ["All", "High-Level", "Detailed", "Refinement"])
            
            filtered_prompts = st.session_state.generated_prompts
            if filter_type == "High-Level":
                filtered_prompts = [p for p in filtered_prompts if p.get('level') == 'high-level']
            elif filter_type == "Detailed":
                filtered_prompts = [p for p in filtered_prompts if p.get('level') == 'detailed']
            elif filter_type == "Refinement":
                filtered_prompts = [p for p in filtered_prompts if p.get('level') == 'refinement']
            
            for idx, saved_prompt in enumerate(filtered_prompts):
                level_badge = saved_prompt.get('level', 'unknown')
                with st.expander(f"{saved_prompt['title']} - {saved_prompt['project_type']} [{level_badge}]", expanded=False):
                    st.text(f"Saved: {saved_prompt['timestamp']}")
                    st.info("Tip: Click in the code box and press Ctrl+A to select all, then Ctrl+C to copy")
                    st.code(saved_prompt['prompt'], language="text")
                    
                    # Three buttons in a clean row
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.download_button(
                            label="📥 Download",
                            data=saved_prompt['prompt'],
                            file_name=f"stitch_prompt_{saved_prompt['title'].replace(':', '_').replace(' ', '_')}.txt",
                            mime="text/plain",
                            key=f"download_saved_{idx}",
                            use_container_width=True
                        )
                    
                    with col2:
                        if st.button(f"🎯 Use for Refinement", key=f"use_saved_{idx}", use_container_width=True):
                            st.session_state.base_prompt = saved_prompt['prompt']
                            st.toast("Prompt loaded for refinement!", icon="🎯")
                    
                    with col3:
                        if st.button(f"🗑️ Delete", key=f"delete_saved_{idx}", use_container_width=True):
                            st.session_state.generated_prompts.pop(idx)
                            st.rerun()
        else:
            st.info("No saved prompts yet. Generate and save prompts from the 'Generate Prompt' tab.")
    
else:
    # Show instructions when no API key is provided
    st.warning("Please enter your Google Gemini API Key in the sidebar to start using the app.")
    
    st.markdown("""
    ### How to get started:
    
    1. **Get a Google Gemini API Key**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey) to create your API key
    2. **Enter your API key** in the sidebar
    3. **Learn Stitch best practices** in the Stitch Guide tab
    4. **Generate optimized prompts** following Stitch guidelines
    5. **Refine screen by screen** for perfect results
    
    ### Features Based on Stitch Official Guide:
    - 📚 Complete Stitch prompt guide with examples
    - 🎯 High-level vs. Detailed prompt generation
    - 🎨 Vibe-setting with adjectives
    - 🔧 Screen-by-screen refinement tools
    - 💾 Save and manage your Stitch prompts
    
    ### Stitch Best Practices:
    - Be Clear & Concise
    - One Major Change at a Time
    - Use UI/UX Keywords
    - Reference Elements Specifically
    - Iterate & Experiment
    """)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit and Google Gemini API | Based on [Stitch Prompt Guide](https://stitch.ai) | [Documentation](https://docs.streamlit.io)")
