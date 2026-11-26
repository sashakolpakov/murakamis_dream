# An actual flat plat for which every MAIN contact fails packing balance

Private analytical note, 31 October 2026. This is an obstruction to selecting
a protected contact to repair complete-radius balance. It is not an obstruction
to the anchored shared-radius criterion or to the volume limit. In fact the
same first-mark source already has a proved anchored certificate.

## 1. Exact original source and its certified packing

Take the actual width-three flat-plat slot word

    (1,3,2,1,3).

The original Morse compiler gives the five ordered quartets

    (1,0,4,2), (2,0,5,3), (4,2,6,5), (1,4,0,6), (6,5,0,3).       (1)

Its white graph is the suspension of the equatorial cycle
0--1--4--5--3--0, with apices 2 and 6. The five MATCHING edges are

    12, 23, 45, 16, 36,

and the ten MAIN edges are

    01, 02, 03, 06, 14, 24, 25, 35, 46, 56.                     (2)

All numbers in these lists are original face labels. This is a simple
triangulated sphere with seven vertices, fifteen edges and ten triangles.
The three original top-cap choices have protected pairs 01, 06, 03.
No abstract matched graph is being substituted for an unverified flat source.

Put z=sqrt(5), r=(3-z)/2 and h=(3+z)/2. With protected lines
0:Y=0 and 1:Y=2, the five finite disks (X,Y,radius) are

    2=(z-1,1,1),       6=(1-z,1,1),
    3=(0,r,r),         4=(0,(1+z)/2,r),
    5=(0,1,z-2).                                               (3)

All twenty finite disk/disk or disk/line support comparisons are exact:
the graph edges are tangent and the nonedges have strict positive slack.
The remaining edge 01 is the contact of the parallel lines at infinity.
The source-compatible right-angled certificate is the one already proved
in the anchored shared-radius note, Section 4; its simple-white construction
retains the displayed matching and literal source pairings.

The resulting curvature vector is

    (0,0,1,h,h,2+z,1).                                        (4)

These are curvatures, not disk radii.

## 2. One common inversion for each possible MAIN mark

For a finite contact p=(p_x,p_y), use the SAME Möbius transformation
w=-1/(z-p) on the whole packing, followed if desired by one rotation
and one positive scale. The two circles incident to p become parallel
cooriented lines. Since every other disk avoids p, all other transformed
disks are bounded and have positive curvature. Before a common rescaling,
the exact curvatures are

    L_0'=2p_y,                 L_1'=2(2-p_y),
    L_f'=[(X_f-p_x)^2+(Y_f-p_y)^2-r_f^2]/r_f,  f=2,...,6.       (5)

For a finite/finite tangency ij the contact used here is

    p=(r_j (X_i,Y_i)+r_i (X_j,Y_j))/(r_i+r_j).                  (6)

For a line/finite contact its coordinates are (X_f,0) or (X_f,2).
For 01 retain the original vector (4). Thus this is a global normalization
of the same labeled packing, not independent local reframing.

Let a port be (x,b,c,y), and set

    X=Q(x,b,y)+Q(x,c,y).

Complete-radius balance requires X>log b and X>log c whenever that
middle is positive. The common-scale cancellation follows from the
actual homogeneity Q(lambda x,lambda b,lambda y)=Q(x,b,y)+log(lambda)/2.

Substituting (3), (5), (6) gives the following exhaustive table. At the
listed zero-based port there is exactly one positive outer variable and
exactly one positive middle; the ratio of the positive middle to the
sum of the outers is ALWAYS h.

| Protected MAIN pair | A failing port |
|---|---:|
| 01 | 0 |
| 02 | 0 |
| 03 | 1 |
| 06 | 3 |
| 14 | 0 |
| 24 | 0 |
| 25 | 1 |
| 35 | 1 |
| 46 | 3 |
| 56 | 4 |

For illustration, the four typed symmetry representatives 01, 02, 14,
24 have, after normalizing the positive outer to one, respectively

    (0,0,h,1), (1,0,h,0), (0,h,0,1), (1,h,0,0)                (7)

at port 0. The exact audit below checks all ten contacts independently,
so the conclusion does not rely on assuming a source adapter for an
abstract symmetry.

## 3. An elementary strict failure uniform over the ten contacts

The absolutely normalized zero-spectral triangle action satisfies

    Q(1,h,0)=F(h)=(2/pi) Ti2(sqrt(h)),  Q(1,0,0)=0,
    Ti2(t)=integral_0^t arctan(s)/s ds.

Write phi=(1+sqrt(5))/2, so h=phi^2. The reciprocal identity
Ti2(t)-Ti2(1/t)=(pi/2)log t gives the common balance difference

    F(h)-log h=(2/pi)Ti2(1/phi)-log phi.                       (8)

This is strictly less than -1/25 by rational elementary bounds:

    phi>8/5,  1/phi<5/8,  Ti2(1/phi)<1/phi,  pi>3,
    log phi>log(8/5)=2 atanh(3/13)>6/13.

Indeed (8) is less than

    (2/3)(5/8)-6/13 = -7/156 < -1/25.                         (9)

The inequalities use only arctan s<s for s>0 and the positive power
series for atanh. Thus every MAIN-contact normalization has a strict
failure, not merely an equality at the boundary of the sufficient test.

Consequently no allowed original cap mark makes this actual plat balanced.
The stronger statement over all ten geometric MAIN contacts remains valid
even if some of those contacts are not allowed as the original top-cap
mark. We do not infer that arbitrary contact relocation preserves the
designated quantum source: the three actual cap choices already suffice,
and enlarging the geometric set only strengthens the negative conclusion.

## 4. Precise consequence and limits

This disproves a universal “choose a better cap mark” repair for complete
packing balance among actual simple-white plats. Combined with the separate
shared-positive-capacity theorem, it also gives a strict exponential loss
for an undivided full positive Cauchy torus at every one of the three allowed
cap marks, even if its ordinary radii depend on N.

It does NOT disprove sector-dependent radius certificates. The existing
anchored theorem supplies six rational whole-vector witnesses for exactly
(1) with protected pair 01, proving its full independently long-filling
volume conclusion. Thus this example separates mark selection from genuine
sector refinement; it does not provide an anchored-criterion counterexample.
No universal filling statement or branched-cover construction follows.

Dependencies in the workspace:

- notes/general_anchored_shared_radius_filling_volume.md, Section 4:
  actual source, exact packing and successful anchored certificate.
- notes/actual_zero_middle_nine_quarter_balance.md, Section 2:
  the source-normalized F/Ti2 identity (used here outside its 9/4 conclusion).
- notes/actual_complete_source_cauchy_capacity_gap.md:
  separate single-torus obstruction, currently under independent review.

Focused exact audit:
/private/tmp/md-audit-all-main-marks-balance-obstruction.py.
It checks original compiler labels, all original supports, the common
inversion at each of the ten MAIN contacts, all positive/zero curvatures,
and the rational bound (9). It does not replace the analytical proof.
