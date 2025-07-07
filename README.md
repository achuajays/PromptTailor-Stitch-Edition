# Stitch UI Prompt Generator 🎨

A Streamlit application that helps generate effective prompts for Stitch AI, following the official Stitch Prompt Guide for building user interfaces.

## Features

- **📚 Stitch Guide**: Complete guide with examples from the official Stitch documentation
- **💡 Sample Ideas**: Browse pre-built UI templates and generate creative ideas with vibe-setting adjectives
- **✨ Dual-Level Prompts**: Generate both high-level (brainstorming) and detailed (specific) prompts
- **🎯 Screen Refinement**: Make specific, incremental changes to individual screens
- **📝 Prompt Management**: Save, filter, and reuse your Stitch prompts
- **🎨 Theme Control**: Specify colors, fonts, borders, and overall vibe following Stitch best practices

## Setup

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/achuajays/PromptTailor-Stitch-Edition.git
cd PromptTailor-Stitch-Edition
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. **Enter your API key**: Add your Google Gemini API key in the sidebar
2. **Learn Stitch Guidelines**: Review the official Stitch prompt guide in the first tab
3. **Choose prompt level**: Select high-level for brainstorming or detailed for specific results
4. **Generate prompts**: Create Stitch-optimized prompts with proper adjectives and structure
5. **Refine screens**: Make specific changes to individual screens following the "one change at a time" principle
6. **Save and reuse**: Filter and manage your prompts by type (high-level, detailed, refinement)

## Application Structure

### Main Components

- **Stitch Guide Tab**:
  - High-level vs. detailed prompts
  - Vibe-setting with adjectives
  - Theme control (colors, fonts, borders)
  - Image modification guidelines
  - Pro tips and best practices

- **Sample Ideas Tab**: 
  - Pre-built templates with vibes
  - AI-generated ideas with adjectives

- **Generate Prompt Tab**:
  - Prompt level selector (high-level/detailed)
  - Vibe adjectives input
  - Theme options (mood-based or specific)
  - Font and button styling
  - Screen-specific generation for detailed prompts

- **Refine Screen Tab**:
  - Base prompt input
  - Screen-specific changes
  - Change types (add/modify components, styling, images, layout, text)
  - Quick refinement templates
  - One change at a time principle

- **Saved Prompts Tab**:
  - Filter by type (high-level, detailed, refinement)
  - Copy, use for refinement, or delete
  - Prompt history management

### Key Classes

```python
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
```

## Example Use Cases

1. **High-Level Brainstorming**: "A vibrant and encouraging fitness tracking app"
2. **Detailed App Creation**: "Product detail page for a Japandi-styled tea store. Neutral colors, minimal design."
3. **Screen Refinement**: "On the homepage, add a search bar to the header"
4. **Theme Changes**: "Update theme to a warm, inviting color palette"
5. **Image Updates**: "Change background of all product images on landing page to light taupe"

## Stitch Best Practices (Built-in)

- **Be Clear & Concise**: Avoid ambiguity in prompts
- **One Major Change at a Time**: Easier to see impact and iterate
- **Use UI/UX Keywords**: navigation bar, CTA button, card layout, etc.
- **Reference Elements Specifically**: "primary button on sign-up form"
- **Set the Vibe**: Always include adjectives to define the app's feel

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License.
