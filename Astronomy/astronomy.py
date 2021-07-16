import numpy as np
import datetime
from decimal import Decimal

"""interesting stuff:
https://docs.sunpy.org/en/stable/generated/gallery/plotting/simple_differential_rotation.html;
"""

# --------------- Variables & Constants ---------------------

# Units
"""[J] = (kg * m^2)/s^2"""

# Constants


class Constant:
    """Sun Radius in meters and the mass of the sun in kg"""
    radius_sun, mass_sun = 6.957e08, 1.989e30
    """Speed of Light in meters"""
    light_speed = 2.99792458e08
    """Astronomical unit in meters"""
    au = 1.49597900e09
    """One au in parsec"""
    au_parsec = 206265
    """Plank Constant h in Js, plank bar constant 'hbar' in Js"""
    plank_constant, plank_bar_constant = 6.62607015e-34, 1.054571817e-34
    """Stefan-Boltzman Constant in J/K"""
    boltzman_constant = 1.380649e-23
    """Days in a year and seconds in a day"""
    """Gravitational constant in m^3 kg^-1 s^-2"""
    gravitational_constant = 6.67408e-11
    """Mass proton in kg and eV"""
    mass_proton_kg = 1.67262192369e-27
    """Mass hydrogen in atomic mass units, kg and eV"""
    mass_hydrogen_u, mass_hydrogen_kg = 1.007825, 1.67e-24
    """Energy of 1eV i J"""
    energy_eV = 1.6e-19
    """pc in meters"""
    parsec = 3.086e+16
    """light year in meters"""
    light_year_meter = 9.461e+15
    """absolute magnitude sun"""
    absolute_magnitude_sun = 4.77
    """luminosity sun in Watt"""
    luminosity_sun = 3.828e26
    """Zero point luminosity in Watt"""
    luminosity_zero_point = 3.0128e28
    """Hubble constant in km/s, different values for the constant depending on measurement, ~4 different ones"""
    hubble_constant = 67.8
    """Days in a year and seconds in a day as well as seconds in a year"""
    days_year, seconds_day, seconds_year = 365.25, 86400, 31557600

# -------------- Classes -----------------------


class Convert:
    """Class to gather all convert functions and convert in any direction"""
    def m_to_pc(self, distance):
        """Converts meter to parsec"""
        return distance/Constant.parsec

    def m_to_au(self, distance):
        """Converts meter to astronomic unit"""
        return distance/Constant.au

    def m_to_lj(self, distance):
        """Converts meter to lightyear"""
        return distance/Constant.light_year_meter

    def au_to_pc(self, distance):
        """Converts astronomic unit to parsec"""
        return distance/Constant.au_parsec

    def au_to_m(self, distance):
        """Converts astronomic unit to meter"""
        return distance*Constant.au

    def au_to_lj(self, distance):
        """Converts astronomic unit to lightyear"""
        pass

    def lj_to_m(self, distance):
        """Converts lightyear to meter"""
        return distance*Constant.light_year_meter

    def lj_to_au(self, distance):
        """Converts lightyear to astronomic unit"""
        pass

    def lj_tp_pc(self, distance):
        """Converts lightyear to parsec"""
        pass

    def pc_to_m(self, distance):
        """Converts parsec to meter"""
        return distance*Constant.parsec

    def pc_to_lj(self, distance):
        """Converts parsec to lightyear"""
        pass

    def pc_to_au(self, distance):
        """Converts parsec to astronomic unit"""
        pass

    def ev_to_joule(self, energy):
        """Converts eV to Joule"""
        return energy/Constant.energy_eV

    def joule_to_ev(self, energy):
        """Converts Joule to eV"""
        return energy*Constant.energy_eV

    def degree_to_radians(self, degree):
        """Converts degree to radians"""
        return degree * (np.pi / 180)

    def radians_to_degree(self, radians):
        """Converts radians to degree"""
        return radians / (np.pi /180)


class Geometrics:
    """Useful geometric formulas"""
    def mass_volume_sphere(self, density, diameter):
        """Calculates the mass and volume of a sphere"""
        volume = 4 / 3 * np.pi * (diameter / 2) ** 3
        mass = volume * density
        return mass, volume

    def volume_torus(self, inner_radius, outer_radius):
        """Is useful for belts, e.g. asteroid or similar"""
        outer_radius, inner_radius = outer_radius * Constant.au, inner_radius * Constant.au
        return 2 * np.pi ** 2 * outer_radius * inner_radius ** 2

# -------------- Methods -----------------------
# Calculate days


def get_days_passed():
    """Gets the days that have passed in the actual year"""
    actual_time = datetime.datetime.now()
    year_ending = actual_time.year - 2000
    days_passed = 0
    for i in range(1, actual_time.month):
        if i < 8:
            if i == 2:
                if year_ending % 4 == 0:
                    days_passed += 29
                else:
                    days_passed += 20
            elif i % 2 == 0:
                days_passed += 30
            else:
                days_passed += 31
        else:
            if i % 2 == 0:
                days_passed += 31
            else:
                days_passed += 30

    days_passed += actual_time.day

    return days_passed


def get_angle_radians(angle):
    """Converts an input angle to radians"""
    return angle * (np.pi / 180)


class ApparentSize:
    """Calculate the size of an object with the angle under which you see it,
    arcminutes are degree/60"""

    def real_size(self, angle_size, distance):
        """Calculates the real size of an object from its apparent size"""
        return 2 * distance * np.tan(Convert().degree_to_radians(angle_size)/2)

    def angle(self, real_size, distance):
        """Calculates the angle of an object from its apparent size"""
        """Calculates the angle of an object from its apparent size"""
        return np.arctan((2 * real_size) / distance) * (180 / np.pi)

    def distance(self, real_size, angle_size):
        """Calculates the distance of an object from its apparent size"""
        return real_size / (2 * np.tan(Convert().degree_to_radians(angle_size) / 2))


class AngularSize:
    """Calculates the angular_size of an object"""
    def angular_size(self, distance, radius=None, angle=None):
        if angle is None:
            res = np.arctan(radius/distance)
            print(f"The angle is {res}")
        if radius is None:
            res = np.tan(angle) * distance
            print(f"The radius of the object ist {res}")


def parallaxis(arcsecs):
    """Takes input in arcseconds and output in parsec and lightyears."""
    if arcsecs < 1:
        res_parsec = 1 / arcsecs
    else:
        au = 150e06
        arcseconds_to_radians = (3600 * arcsecs) * (np.pi/180)
        res = au / np.tan(arcseconds_to_radians)
        res_parsec = res/206265

    res_lj = res_parsec * 3.26
    print(f"The distance is {round(res_parsec, 2)}pc, which is {round(res_lj, 2)} Lightyears.")
    return res_parsec, res_lj


# Berechnung der absoluten Helligkeit
def magnitude(distance: "In parsec", absolute_magnitude):
    """calculates the magnitude of a star"""

    magnitude = 5 * np.log10(distance/10) + absolute_magnitude
    print(f"The apparent magnitude is {round(magnitude, 2)}")

    return magnitude


def absolute_magnitude(distance: "In parsec", magnitude):
    """Calculates the absolute magnitude of a star"""

    absolute_magnitude = magnitude - 5 * np.log10(distance / 10)
    print(f"The magnitude is {round(absolute_magnitude, 2)}")

    return absolute_magnitude


def absolute_magnitude_from_luminosity(luminosity: "Input in luminosity of the sun"):
    """Calculates the abosulte magnitude from the suns luminosity"""
    return round(-2.5*np.log10(luminosity/Constant.luminosity_zero_point), 2)


def magnitude_difference(magnitude):
    """Calculates the brightness of the magnitude of a star"""
    return 2.512**magnitude


def distance_modulus(magnitude, absolute_magnitude):
    """Calculates the distance of stars via their apparent magnitude and the absolute magnitude.
    Result is in parsec."""
    return 10**((magnitude-absolute_magnitude+5)/5)*10


def sunrise_equation(latitude):
    sun_declination = 0.4095 * np.sin(0.016906 * (get_days_passed() - 80.086))
    res = -np.tan(latitude) * np.tan(sun_declination)
    # the sign determines the sunrise (negative value) and or sunset (positive value)
    sunrise = round(15/np.arccos(-res), 2)
    sunset = round(15/np.arccos(res), 2)
    if sunrise > 24:
        sunrise -= 24
        sunrise = str(round(sunrise, 2)) + " am"
    return sunrise, sunset


class WienschesGesetz:
    """Calculates the peak wavelength an objects emits at certain temperatures"""
    def __init__(self):
        # check which constant that is
        self.constant = 2.879e-03

    def small_values_wavelength(self, temperature):
        """Calculates the peak emitted wavelength of an object from its temperature"""
        return self.constant/temperature

    def small_values_temperature(self, max_wavelength):
        """Calculates the temperature of an object from its peak emitted wavelength"""
        return self.constant / max_wavelength


def stefan_boltzman(temperature):
    """Calculates the power of radtiation emitted by some object"""
    sigma = (2*(np.pi**5)*(Constant.boltzman_constant**4))/(15*(Constant.plank_constant**3)*(Constant.light_speed**2))
    return sigma * (temperature**4)


def effective_temperature(radiant_excitance):
    """Calculates an objects effective temperature"""
    sigma = (2*(np.pi**5)*(Constant.boltzman_constant**4))/(15*(Constant.plank_constant**3)*(Constant.light_speed**2))
    return (radiant_excitance/sigma)**(1/4)


def luminosity(distance, irradiance):
    """Earth e.g. is tiny square of surface of imaginary sphere that contains the whole luminosity of e.g. sun"""
    # "https://socratic.org/questions/how-can-you-calculate-solar-luminosity-of-the-sun-using-earth-s-solar-constant"
    # Also possible to use Stefan-Boltzman Law that yieds L = sigma * A * T**4
    return 4 * np.pi * irradiance * (distance**2)


def specific_excitance(luminosity, radius):
    return luminosity/(4*np.pi*(radius**2))


def effective_heat(spec_excitance):
    return (spec_excitance/5.67e-08)**(1/4)


def kinetic_energy_asteroid(density, diameter, speed):
    relative_mass = Geometrics().mass_volume_sphere(density, diameter)[0]/(np.sqrt(1-(speed/Constant.light_speed)**2))
    E_rel = 1/2 * relative_mass * speed**2
    E = 1/2 * Geometrics().mass_volume_sphere(density, diameter)[0] * speed**2
    return E, E_rel


def density(volume, mass):
    return mass/volume


def freie_weglaenge(diameter_objects, number_of_particles):
    """asteroidengürtel oder ähnliches. Für zwei gleiche objekte die sich ungeordnet bewegen"""
    lam = 1/(np.sqrt(2)*np.pi*number_of_particles*diameter_objects**2)
    return lam


def gleichgewichtstemperatur(albedo, distance_sun):
    temp_eff_sun = 5772, 696342
    temperature = (1 - albedo)**(1/4) * temp_eff_sun * np.sqrt(Constant.radius_sun/(2 * distance_sun))
    return temperature


def tangential_velocity(mu,  distance: "In parsec"):
    """mu ist die senkrecht zur radialgeschwindigkeit angegebene komponente"""
    """Für kleine Winkel mit der  Umrechnung von AE/Jahr in km/s erhält man den Vorfaktor 4.74"""
    return 4.74 * mu * distance


def true_velocity(radial_velocity, tangential_velocity):
    velocity = np.sqrt(radial_velocity**2 + tangential_velocity**2)
    return velocity


def photon_star_escape_travel_time_and_distance(free_middle_length_in_star, radius_star):
    number_of_collisions = (radius_star / free_middle_length_in_star)**2

    total_distance = number_of_collisions * free_middle_length_in_star
    # time in seconds
    travel_time_to_surface_seconds = total_distance / Constant.light_speed
    # convert to years
    travel_time_to_surface_year = travel_time_to_surface_seconds/(60*60*24*365.25)

    return number_of_collisions, total_distance, '%.2e' % Decimal(travel_time_to_surface_year)


def energy_density(energy, volume):
    return energy/volume


def rotational_velocity_on_sun_surface(start_cycle, end_cycle):
    # Umrechnen von Tag in sekunde
    differential_rotation_start = (14.38-2.88*np.sin(get_angle_radians(start_cycle))**2) * 60 * 60 * 24
    differential_rotation_end = (14.38-2.88*np.sin(get_angle_radians(end_cycle))**2) * 60 * 60 * 24

    return differential_rotation_start * Constant.radius_sun * 1e-03,\
           differential_rotation_end * Constant.radius_sun * 1e-03


def loss_of_mass_by_solarwind(distance_from_star, density_of_particles, velocity_of_solarwind):
    """The amount of mass lost by a star in a year in sun masses"""
    radius_solar_globe_cm = distance_from_star
    velocity_of_solarwind_cm_year = velocity_of_solarwind * 1e05/(Constant.days_in_year*Constant.seconds_in_day)

    loss_of_mass = 4*np.pi*(radius_solar_globe_cm**2)*density_of_particles*velocity_of_solarwind_cm_year

    return loss_of_mass/Constant.mass_sun


def mean_molecular_mass_gascloud(*args: list):
    """This calculates the mean molecular weight 'mu' per particle,
    Input in lists [Number_of_particles, nucleon_number, percentage_of_mass_of_cloud]"""
    number_of_particles, nucleon_mass, percentage_of_mass = [], [], []
    mean_mass = 0

    # sets the arguments to the correct parameters
    for i in args:
        number_of_particles.append(i[0])
        nucleon_mass.append(i[1])
        percentage_of_mass.append(i[2])

    for i in range(len(number_of_particles)):
        mean_mass += (number_of_particles[i]/nucleon_mass[i])*percentage_of_mass[i]

    return round(1/mean_mass, 2)


def molar_mass(mass, molar_mass):
    """Calculates the number of moles of object with mass"""
    return mass/molar_mass


def jeans_radius(mass_cloud, mean_molecular_mass, temperature):
    """Outputs the radius of a gas cloud at the jeans critical point in meters"""
    return (Constant.gravitational_constant * mass_cloud * mean_molecular_mass * Constant.mass_proton_kg) / \
           (5 * Constant.boltzman_constant * temperature)


def cloud_radius_after_ionization(mass_cloud, radius_jeans):
    """Calculates the radius of a gas cloud after ionization and further contraction"""
    factor = 5/(3*Constant.gravitational_constant*(mass_cloud**2))
    right_hand_side = (4.5*mass_cloud)/(2*Constant.mass_hydrogen_kg*Constant.energy_eV) +\
                      (13.6*mass_cloud)/(Constant.mass_hydrogen_kg*Constant.energy_eV)

    return (factor * right_hand_side + 1/radius_jeans)**(-1)


def verweildauer(mass_star_norm_sun):
    """Calculates the 'Verweildauer' of a star in the HR in the HDR
    takes the mass of a star in sun masses.
    1 stands for the mass of the sun. Result is given in years"""
    return 10e09 * ((mass_star_norm_sun/1)**(-2))


def mass_loss_agb_phase(mass_star_norm_sun, radius_star_norm_sun, luminosity_star_norm_sun):
    """This calculates the rate of mass lost dM/dt during the transition
    from the helium phase to the AGB(Asypmtotic Giant Branch)-phase of a star
    Every 1 here is the respective term for the sun. The result is also in sun masses.
    Input values also in respect to the sun"""
    return -4e-13 *(1/mass_star_norm_sun) * (radius_star_norm_sun/1) * (luminosity_star_norm_sun/1)


def white_star_core_radius(star_core_mass_norm_sun):
    """This calculates the radius a white star has left after the outer shell has been radiated away
    All values are in respect to the suns.
    Returns the white stars radius in respect to the suns"""
    return star_core_mass_norm_sun**(-1/3)


def rest_mass_energy(mass, velocity):
    """Calculates the resting mass of an object. Part of the special relativity"""
    relativistic_mass = mass*(1/np.sqrt(1-(velocity/Constant.light_speed)**2))
    return relativistic_mass*(Constant.light_speed**2)


def moment_of_inertia(mass, radius):
    """This calculates the moment of intertia for an object of mass m and radius r"""
    return (2/5)*mass*(radius**2)


def rotational_energy(moment_of_inertia, circular_frequency):
    """Calculates the rot energy"""
    return 0.5*moment_of_inertia*(circular_frequency**2)


def age_of_pulsar(period_of_rotation_in_seconds, decrease_of_rotation_rate_per_second):
    """Calculates the age of a pulsar via its rotation.
     Takes values in seconds and seconds/second. Returns age in years"""
    return round(
        0.5*(period_of_rotation_in_seconds/decrease_of_rotation_rate_per_second)/\
        (Constant.seconds_in_day*Constant.days_in_year), 2)


def magnetic_field_pulsar(period_of_rotation_in_seconds, decrease_of_rotation_rate_per_second):
    """Returns minimum magnetic field of pulsar via its period and decay of said period"""
    return 3.2e19*((period_of_rotation_in_seconds*decrease_of_rotation_rate_per_second)**(1/2))


def photon_energy(wavelength):
    """Calculates the energy of a photon from its wavelength"""
    return (Constant.plank_constant*Constant.light_speed)/wavelength


def photon_luminosity_B_seq_star(luminosity, wavelength):
    """Returns the number of photons emitted by second of a B sequence star.
    Output in photons/second."""
    frequency = Constant.light_speed/wavelength
    return luminosity/(Constant.plank_constant*frequency)


def stroemgren_radius(recombination_time, mean_middle_free_length, photon_luminosity):
    """Returns the radius of the strömgren sphere in meters, lightyears and parsec"""
    denominator = 3*photon_luminosity
    nominator = 4*np.pi*(mean_middle_free_length**2)*recombination_time
    return (denominator/nominator)**(1/3), (denominator/nominator)**(1/3)/Constant.parsec,\
           (denominator/nominator)**(1/3)/Constant.light_year_meter


def tully_fisher(max_rotational_speed):
    """Distance relation without standard torch. Calculates distance via the rotational speed and the luminosity
    of the galaxy.
    Calculates the absolute blue luminosity. Input values are km/s"""
    return -9.95*np.log(max_rotational_speed/1)+3.15


def schwarzschild_radius(mass):
    """Calculates the radius of an object that turns into a black hole."""
    return (2 * Constant.gravitational_constant * mass) / (Constant.light_speed**2)


class Eddington:
    """This calculates the eddington luminosity of a blazar"""
    def luminosity(self, center_mass):
        return 3.2e04 * (center_mass / Constant.mass_sun) * Constant.luminosity_sun

    def mass_center(self, eddington_luminosity):
        return (eddington_luminosity * Constant.mass_sun) / (3.2e04 * Constant.luminosity_sun)

    def accreation_rate(self, eddington_luminosity, center_mass, radius):
        """Calculates the rate at which the disk acquires mass"""
        efficiency = (Constant.gravitational_constant * center_mass) / (radius * (Constant.light_speed**2))
        return eddington_luminosity / (efficiency * (Constant.light_speed**2)), efficiency


def mass_galaxy_viral(velocity_dispersion, radius_galaxy):
    """Calculates the mass of a galaxy from its radius and velocity dispersion"""
    return ((velocity_dispersion**2) * radius_galaxy) / Constant.gravitational_constant


def distance_fundamental_plane(velocity_dispersion):
    """Calculates the distance to an object with the law of the fundamental plane using the velocity dispersion.
    Output in kpc"""
    return 2.05 * ((velocity_dispersion/100)**1.33)


def hubble_law(distance):
    """Calculates the reccesion velocity of a galaxy. Describes the relation between 'seen' velocity and distance.
    Distance D is measured in Mpc."""
    return Constant.hubble_constant * distance


if __name__ == "__main__":
    print(tully_fisher(325))
    print(distance_modulus(12.2, -54.4))
    print((Eddington().mass_center(10e39))/Constant.mass_sun)
    print(Eddington().accreation_rate(10e39, 816353187.0428424, 3*schwarzschild_radius(816353187.0428424)))
    print((Eddington().accreation_rate(10e39, 816353187.0428424,
                                       3*schwarzschild_radius(816353187.0428424)))[0] / Constant.mass_sun)
    print((mass_galaxy_viral(600e03, Convert().pc_to_m(1.5e06)))/Constant.mass_sun)
    print(hubble_law(distance_fundamental_plane(600)))
    print(Convert().pc_to_m(1.5e06)/1506.345928481908e03)
    print(3.0729993107659508e+16/Constant.seconds_year)
