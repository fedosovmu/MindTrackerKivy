from kivy.uix.screenmanager import Screen


class MoodAssessmentScreen(Screen):
    def __init__(self, **kwargs):
        super(MoodAssessmentScreen, self).__init__(**kwargs)
        self.set_bindings()
        print('MoodAssessmentScreen init')
    
    def set_bindings(self):
        mood_assessor_slider = self.ids.mood_assessor.ids.mood_assessor_slider
        mood_assessor_slider.fbind('value', self.mood_assessor_slider_on_value_changed)
        #print(self.ids)

    def mood_assessor_slider_on_value_changed(self, instance, value):
        print(f'Mood assessment changed {value}')
        #mood_sphere_image = self.screen_manager.ids.mood_assessment_screen.ids.mood_assessor.ids.mood_sphere_image
        #mood_sphere_image.source = f'data/images/mood_spheres/{value}.png'
        #mood_agree_button = self.ids.mood_assessment_screen.ids.mood_agree_button
        #mood_agree_button.current_mood = value
