from .hittable import Hittable
from .hit_record import HitRecord

class HittableList(Hittable):
    def __init__(self, hittables):
        self.hittables = hittables

    def hit(self, ray, t_min, t_max, rec):
        hit_anything = False
        closest_so_far = t_max
        temp_rec = HitRecord()
        for hittable in self.hittables:
            if hittable.hit(ray, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.t = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
        return hit_anything