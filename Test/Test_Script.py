from selenium import webdriver

from POM.GetPopulationCountClass import GetPopulationCount

URL = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"

def test_get_population_count(browser_start):
    driver = browser_start
    population_count = GetPopulationCount(driver)
    population_count.OpenUrl(URL)
    population_count.get_population_count()




