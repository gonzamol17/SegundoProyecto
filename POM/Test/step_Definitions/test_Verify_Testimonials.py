import time
from pytest_bdd import scenarios, given, when, then
from colorama import Fore, Back, Style
from POM.Pages.MyAccountPage import MyAccountPage

scenarios('../features/Verify_Testimonials.feature')

@given("I am on the Automation test")
def step_GoAutomationStore(test_setup):
    time.sleep(2)


@when("I scroll to the bottom of the screen, and check each of the items in the Testimonials section", target_fixture='t')
def step_CheckItems(test_setup):
    account = MyAccountPage(test_setup)
    test_setup.execute_script("window.scrollTo(0, 4000)")
    t = account.getTestimonials()
    return t

@then("I verify each existing testimonial, and print them")
def step_VerifyAndPrintTestimonials(t, test_setup):
    #driver = test_setup
    expected_texts = [
        "Regular customer and products",
        "Returns were easy and my",
        "I found this store to be very reasonably",
        "Really great products"
    ]
    position_names = ['Sub_cero', '1er', '2do', '3er', '4to', '5to']

    print("\n")
    n = 0
    for testimonial in t:
        if n == 0 or n == 5:
            # Saltamos las posiciones que no necesitamos verificar
            n += 1
            continue


        # Validación correcta: assert que el texto del testimonial contenga alguna de las opciones esperadas
        assert any(exp_text in testimonial.text for exp_text in expected_texts), \
            f"Testimonial no esperado: {testimonial.text}"

        print(Fore.GREEN + f"El título del {position_names[n]} Testimonials es: " + Fore.RESET + testimonial.text)
        n += 1
        time.sleep(1)

