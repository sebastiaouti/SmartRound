# SmartRound

Simple Streamlit app with two modules:
- **SmartCheck**: small lab exam checker example.
- **SmartRound**: generates a short medical note using OpenAI and allows export to DOCX.

## Setup
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key (if using AI generation):
   ```bash
   export OPENAI_API_KEY=YOUR_KEY
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Manual testing
The app was launched locally and the forms were exercised with example inputs. Text generation via OpenAI and the DOCX export button were triggered to ensure there were no runtime errors.
