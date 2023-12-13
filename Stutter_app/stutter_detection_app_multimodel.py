import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior

# import classes 

from features import StutterFeatureExtractor
from hyperlink_label import HyperlinkLabel

class_to_type = {
    0: 'Block',
    1: 'Interjection',
    2: 'NoStutterWords',
    3: 'WordRep',
    4: 'SoundRep',
    5: 'Prolongation'
}

# Detailed stutter information
stutter_info = {
    0: {
        'title': 'Blocks',
        'text': '''Blocks are pauses in speech that occur when the person is unable to produce a sound or word. For example, someone who stutters might say "I want a (pause) cookie" instead of "I want a cookie."

Blocks can be very frustrating and embarrassing for people who stutter. They can make it difficult to communicate effectively and can lead to social anxiety.
There is no one-size-fits-all cure for blocks. 

Therapy suggestions for Block: 
However, there are a number of therapy techniques that can help people who stutter to manage their blocks and improve their fluency. Some common therapy techniques for blocks include:
•Easy onset: This technique involves learning to start words smoothly. This can be done by practicing slowing down speech rate and relaxing the muscles in the mouth and throat.
•Prolonged speech: This technique involves speaking slowly and deliberately. This can help to break the pattern of blocks.
•Cancellation: This technique involves learning to stop a block. This is done by taking a deep breath and tensing the muscles in the mouth and throat.


In addition to therapy, there are a number of self-help strategies that people who stutter can use to manage their blocks. These strategies include:

•Being patient with yourself: It takes time and practice to learn to manage blocks. Don't get discouraged if you don't see results immediately.
•Practicing speaking aloud: The more you practice speaking, the more comfortable you will become and the less likely you are to block.
•Joining a support group: Talking to other people who stutter can help you to feel less alone and can provide you with valuable support and encouragement.
''',
        'links': ['https://stutteringtherapist.com/stuttering-blocks-and-how-we-can-stop-them/', 'https://youtu.be/wDd3PfH_JJI?si=GUcZP1MMNRsVAyQu&t=35']
    },
    1: {
        'title': 'Interjection',
        'text': '''Interjections are filler words or sounds that are used to fill in gaps in speech. They are a common feature of speech, and they are used by both people who stutter and people who do not stutter. However, people who stutter may use interjections more frequently than people who do not stutter.
For example, someone who stutters might say "Um, I need to go home" instead of "I need to go home."

Interjections can be used for a variety of reasons, including:
•To buy time: When a person who stutters is struggling to say a word, they may use an interjection to buy themselves some time to regain their fluency.
•To mask a stutter: Sometimes, people who stutter may use interjections to mask or hide their stuttering. This can be a way of trying to avoid negative attention or embarrassment.
•To maintain fluency: In some cases, interjections can actually help to maintain fluency. For example, someone who stutters may use a filler word like "um" or "uh" to start a word that they are having trouble with.
However, interjections can also have some negative consequences for people who stutter.
•They can increase anxiety: Interjections can sometimes increase anxiety, which can make stuttering worse.
•They can interrupt the flow of speech: Interjections can interrupt the flow of speech and make it more difficult to communicate effectively.
•They can make stuttering more noticeable: Interjections can draw attention to stuttering and make it more noticeable to others.

Therapy Techniques for interjections:

•Be aware of your interjection usage: The first step is to become aware of how often you use interjections. You can do this by recording yourself speaking or keeping a log of your interjections.
•Identify the triggers: Once you know how often you use interjections, you can start to identify the triggers that cause you to use them. For example, you may find that you use interjections more often when you are anxious or stressed.
•Use alternative strategies: There are other strategies you can use to manage stuttering, such as slowing down your speech rate or using fluency-shaping techniques.
•Practice mindfulness: Mindfulness techniques can help you to become more aware of your thoughts and feelings, which can make it easier to manage your use of interjections.

''',
        'links': ['https://youtu.be/66yiLTgAqtw?si=Y9dZ6zJEI1NomhX_&t=30', 'https://qr.ae/pKkvOw']
    },
    3: {
        'title': 'Word repetition',
        'text': '''Word repetition is a common type of stuttering, characterized by the repetition of one or more words in spoken language. It may manifest as one of several forms:
•Whole-word repetition: This involves saying the same word two or more times in a row. For instance, someone who stutters might say "I w-w-w-want a drink" instead of "I want a drink."
•Part-word repetition: This involves repeating a part of a word, such as a syllable or sound. For example, someone who stutters might say "I-m-m-m-m going to the store" instead of "I'm going to the store."

Word repetition can be caused by various factors, including:
•Anxiety: Anxiety can lead to increased tension in the speech muscles, which can make it difficult to produce words smoothly.
•Muscle tension: Muscle tension can also be caused by fatigue, stress, or other factors.
•Brain activity: Some studies suggest that word repetition may be related to how the brain processes language.
Therapy suggestions for word repetition:
•Easy onset: This technique involves learning to start words smoothly. This can be done by practicing slowing down speech rate and relaxing the muscles in the mouth and throat.
•Prolonged speech: This technique involves speaking slowly and deliberately, stretching out each sound slightly. This can help to break the pattern of word repetitions.
•Cancellation: This technique involves learning to stop a word repetition. This is done by taking a deep breath and tensing the muscles in the mouth and throat.
•Visualization: This technique involves visualizing yourself speaking fluently. This can help to reduce anxiety and improve your overall speech production.
•Biofeedback: This technique involves using electronic devices to monitor and help you control your speech muscles.

''',
        'links': ['https://youtu.be/dj4IQl7h1FM?si=icFZ7oer1bQAUufK&t=70', 'https://qr.ae/pKkn3Y']
    },
        4: {
        'title': 'Sound repetition',
        'text': '''Sound repetition is a common type of stuttering, characterized by the repetition of one or more sounds in a spoken word. It may manifest as one of several forms:

•Initial sound repetition: This involves repeating the first sound of a word. For example, someone who stutters might say "K-k-k-k-car" instead of "car."
•Medial sound repetition: This involves repeating a sound in the middle of a word. For example, someone who stutters might say "Po-po-po-po-table" instead of "table."
•Final sound repetition: This involves repeating the last sound of a word. For example, someone who stutters might say "Do-do-do-do-g" instead of "dog."
Sound repetition can be caused by various factors, including:
•Anxiety: Anxiety can lead to increased tension in the speech muscles, which can make it difficult to produce sounds smoothly.
•Muscle tension: Muscle tension can also be caused by fatigue, stress, or other factors.
•Brain activity: Some studies suggest that sound repetition may be related to how the brain processes language.


Therapy suggestions for sound repetition:

•Easy onset: This technique involves learning to start words smoothly. This can be done by practicing slowing down speech rate and relaxing the muscles in the mouth and throat.
•Prolonged speech: This technique involves speaking slowly and deliberately, stretching out each sound slightly. This can help to break the pattern of sound repetitions.
•Cancellation: This technique involves learning to stop a sound repetition. This is done by taking a deep breath and tensing the muscles in the mouth and throat.
•Visualization: This technique involves visualizing yourself speaking fluently. This can help to reduce anxiety and improve your overall speech production.
•Biofeedback: This technique involves using electronic devices to monitor and help you control your speech muscles.

''',
        'links': ['https://www.medicalnewstoday.com/articles/321995#long-term-treatments', 'https://youtu.be/-1U-iEYLKaA?si=FpeABK6Tx-0kY6jU']
    },
    5: {
        'title': 'Prolongations',
        'text': '''Prolongation is when a sound is stretched out for longer than it should be. For example, someone who stutters might say "Sssssssammy" instead of "Sammy." 

Prolongation is caused by a number of factors, including: 
Anxiety: Anxiety can cause the muscles in the mouth and throat to tense up, which can make it difficult to produce sounds smoothly. Muscle tension: Muscle tension can also be caused by fatigue, stress, or other factors. Neurological factors: Some people who stutter have neurological conditions that can affect their speech.

Therapy suggestions for prolongation: 
•Slowing down speech rate: This can help to reduce the likelihood of prolongations.

•Practicing relaxation techniques: This can help to reduce anxiety and tension, which can contribute to prolongations. 

•Using a fluency shaping technique: This is a type of therapy that helps people who stutter to control their breathing and muscle movements while speaking.

one thing I came to know is it's all in your mind. If you can control your mind believe me you can control your stuttering. Your mind is the most powerful force you will ever face. It always wants to remain in comfort zone hence it tricks! It tells you; you can't do that. You aren't good enough for that, you aren't meant for that. All you have to do is don't listen to its opinions. Force your mind to thinking positive and you'll see a lot of improvement! I also found people who stutter are very Sharp compared to others and are really honest and loving. Love to all those people who stutter  . I can understand your pain and frustration.
''',
        'links': ['https://youtu.be/aP3gksGRqMM?si=a6mAxTwtzJa7y8mL', 'https://youtu.be/wDd3PfH_JJI?si=GUcZP1MMNRsVAyQu&t=35']
    }
}



class StutterDetectionApp(App):
    def build(self):
        self.title = 'Stutter Detection App'
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.file_chooser = FileChooserListView(filters=['*.wav'])
        layout.add_widget(self.file_chooser)

        predict_btn = Button(text='Detect Stutter', size_hint=(1, 0.1))
        predict_btn.bind(on_press=self.show_solution)
        layout.add_widget(predict_btn)

        self.result_label = Label(text='Please select a .wav file and click Detect Stutter')
        layout.add_widget(self.result_label)

        return layout

    def show_info_popup(self, stutter_type):
        info = stutter_info.get(stutter_type, {})
        if info:
            popup_layout = BoxLayout(orientation='vertical', spacing=20)
            title_label = Label(text=info.get('title', ''), size_hint_y=None, height=40)
            popup_layout.add_widget(title_label)

            scroll_view = ScrollView(size_hint=(1, None), size=(400, 500))
            content_layout = BoxLayout(orientation='vertical', size_hint_y=None)
            content_layout.bind(minimum_height=content_layout.setter('height'))

            text_label = Label(text=info.get('text', ''), size_hint_y=None, halign="left", valign="top")
            text_label.bind(width=lambda *x: text_label.setter('text_size')(text_label, (text_label.width - 10, None)),
                            texture_size=lambda *x: setattr(text_label, 'height', text_label.texture_size[1]))
            content_layout.add_widget(text_label)

            for link in info.get('links', []):
                link_label = HyperlinkLabel(text=link, url=link, size_hint_y=None, height=30)
                content_layout.add_widget(link_label)

            scroll_view.add_widget(content_layout)
            popup_layout.add_widget(scroll_view)

            popup = Popup(title='Stutter Information', content=popup_layout, size_hint=(0.9, 1.05))
            popup.open()

    def show_solution(self, instance):
        selected = self.file_chooser.selection
        if selected:
            audio_file_path = selected[0]
            model_path = 'models/lstm_model_multiclass.h5'
            scaler_path = 'models/scaler_for_multiclass.joblib'
            # Create an instance of StutterFeatureExtractor
            stutter_extractor = StutterFeatureExtractor(model_path, scaler_path)

            predicted_class = stutter_extractor.predict_stutter_type(audio_file_path)
            predicted_type = class_to_type.get(predicted_class, 'Unknown')
            self.result_label.text = f'Predicted Stutter Type: {predicted_type}'
            
            if predicted_class not in [2]:  # If not NoStutterWords
                self.show_info_popup(predicted_class)
        else:
            self.result_label.text = 'No file selected'

if __name__ == '__main__':
    StutterDetectionApp().run()



#to the run the code: python stutter_detection_app_multimodel.py