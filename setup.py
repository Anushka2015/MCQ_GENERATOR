from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Anushka Srivastava',
    author_email='anushka.asthana1983@gmail.com',
    install_requires=["openai","huggingface","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)