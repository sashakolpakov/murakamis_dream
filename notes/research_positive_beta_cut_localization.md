# Positive beta cut densities and actual real-latitude localization

Private written proof, 18 November 2026.

The original unmarked scalar admits a positive cut density whose
mass outside any fixed neighborhood of the middle latitude is
superexponentially small in the level. The estimate holds for
the absolute value of the full literal finite Gaussian network,
before contraction. It retains every physical occupation and
the complete marked Ward defect.

The density has degree \(2N^2\). Its original normal-residue
representative and current are kept at that degree. No reduction
to the canonical degree-\(N-1\) Toeplitz representative is made.
The five complete proof sources S, G, T, J and C are pinned below.

## 1. A positive trace-one physical cut

Put \(N\ge2\), \(d=N-1\), and let \(m\ge1\) be an integer.
Use the actual factorial basis and all original pivots and
framing factors of S and G. Define
\[
 q_m(T)=\frac{T^m(1-T)^m}{B(m+1,m+1)},\qquad
 B_{a,d}(T)=\binom da T^a(1-T)^{d-a},
\]
\[
 w_{m,a}=\int_0^1q_m(T)B_{a,d}(T)\,dT,\qquad
 P_{N,m}=\sum_{a=0}^d w_{m,a}T_a .
 \tag{1}
\]
Here \(T_a\) is the literal coordinate projection. The elementary
factorial beta integral gives
\[
 w_{m,a}
 =\binom da\frac{B(a+m+1,d-a+m+1)}{B(m+1,m+1)}
 =\binom da\frac{(m+1)_a(m+1)_{d-a}}{(2m+2)_d}.
 \tag{2}
\]
Rising factorials are used in the last expression.
All weights are positive, symmetric under \(a\mapsto d-a\),
and sum to one, since \(\sum_a B_{a,d}=1\).

S supplies the actual unmarked one-cut identity
\(C_N(M)=F_N(M)I\). Consequently
\[
 \operatorname{Tr}(P_{N,m}C_N(M))
 =F_N(M)=\operatorname{Tr}(T_0C_N(M)).
 \tag{3}
\]
This is a whole meridian-germ identity with the same reduced
scalar normalization. If the original presentation includes
the modified-dimension factor, that whole factor multiplies
both sides. In particular (3) is the original scalar at \(M=1\).

For an arbitrary marked matrix \(C\), the difference is retained.
Write \(Q=e^{2\pi i/N}\) and
\[
 \epsilon_r(M)=MQ^{-r-1}-M^{-1},\qquad
 B_{N,m}=-\sum_{r=0}^{d-1}
       \frac{\sum_{a>r}w_{m,a}}{\epsilon_r(M)}E_{r+1,r}.
 \tag{4}
\]
The actual raising-arrow calculation in S, or its direct
telescoping sum, gives
\[
 [\mathcal E,B_{N,m}]=P_{N,m}-T_0,\qquad
 \operatorname{Tr}((P_{N,m}-T_0)C)
 =\operatorname{Tr}(B_{N,m}[C,\mathcal E]).
 \tag{5}
\]
The cumulative weights lie in \([0,1]\). Thus the same physical
coefficient bounds of S imply, uniformly in \(m\),
\[
 \|B_{N,m}\|\le N/3\quad (|M-1|\le1/(4N)),\qquad
 \|\partial_M^jB_{N,m}\|\le C_jN^{j+1}
       \quad (|M-1|\le1/(8N)).
 \tag{6}
\]
These are the norms and basis convention of S. The original
tail pivots and marked commutator are not changed.

## 2. Concentration of the density and the exact weight ratio

Let \(A_m=q_m(1/2)\). Then
\[
 A_m=(2m+1)4^{-m}\binom{2m}{m}\le2\sqrt{m+1},
 \qquad
 q_m(T)=A_m[1-4(T-1/2)^2]^m.
 \tag{7}
\]
For completeness, \(c_m=4^{-m}\binom{2m}{m}\) satisfies
\(c_m/c_{m-1}=(2m-1)/(2m)\). Induction gives
\(c_m^2\le1/(m+1)\): the induction step reduces to
\((2m-1)^2(m+1)\le4m^3\), valid for \(m\ge1\).
This proves the bound in (7).
For \(0<\varepsilon<1/2\), it follows that
\[
 \int_{|T-1/2|\ge\varepsilon}q_m(T)\,dT
 \le 2\sqrt{m+1}\,e^{-4m\varepsilon^2}.
 \tag{8}
\]
All fixed real derivatives have polynomial bounds. Indeed, on
\(|z-T|\le1/(m+1)\), \(T\in[0,1]\),
\[
 |z(1-z)|\le1/4+(m+1)^{-1}+(m+1)^{-2}.
\]
The maximum modulus bound and Cauchy's formula therefore give
\[
 \|q_m^{(j)}\|_{[0,1]}
 \le j!e^8 A_m(m+1)^j .
 \tag{9}
\]
This uses a shrinking complex collar, not a fixed complex tube.

The exact adjacent-weight ratio is
\[
 \frac{w_{m,a+1}}{w_{m,a}}
 =\frac{d-a}{a+1}\frac{a+m+1}{d-a+m},
 \qquad 0\le a<d.
 \tag{10}
\]
Let \(\pi_a=2^{-d}\binom da\). Expanding (2) gives
\[
 \log\frac{w_{m,a}}{\pi_a}
 =\sum_{i=0}^{a-1}\log\left(1+\frac{i}{m+1}\right)
 +\sum_{i=0}^{d-a-1}\log\left(1+\frac{i}{m+1}\right)
 -\sum_{i=0}^{d-1}\log\left(1+\frac{i}{2(m+1)}\right).
 \tag{11}
\]
Empty sums are zero. Since \(0\le\log(1+t)\le t\) for \(t\ge0\),
\[
 \left|\log\frac{w_{m,a}}{\pi_a}\right|
 \le\frac{3d(d-1)}{4(m+1)}
 \quad\hbox{for every }0\le a\le d.
 \tag{12}
\]
We henceforth choose \(m=N^2\). Equation (12) gives a uniformly
bounded relative weight, not a relative-error comparison of
oscillatory contractions. The exact equality of scalars is (3).

The principal cut action is also unchanged. In J's notation
\(h=2\pi i/N\), \(u=ha\), \(c_0=2\pi i\), the first factor
in (10) is \((c_0-h-u)/(u+h)\). The second factor is
\[
 \frac{m+1+u/h}{m+d-u/h}=1+O(N/m)
 \tag{13}
\]
uniformly on each fixed complex \(u\)-compact. Its denominator
is a unit there for large \(N\). Equation (12) shows that its
integrated contribution has zero \(h^{-1}\) principal action.
Thus J's interior principal cut row and its localized stationary
ideal remain those of the binomial cut. This statement uses
exactly J's unit, logarithm-sheet and canonical-relation scope;
it does not supply a phase for the full coherent crossing sum.

## 3. The exact Gaussian source at every real latitude

Use G's literal two-mode kernel
\[
 \mathcal K_C(Z,\overline W)
 =\frac1{d!}\sum_{i,j=0}^d C_{ij}\binom dj
       Z_1^iZ_0^{d-i}\overline W_1^{\,j}
                              \overline W_0^{\,d-j}.
 \tag{14}
\]
Its metric, Gaussian composition and total-degree projectors
are unchanged. Set
\[
 Z_d(v,T)=\sqrt d\,(\sqrt{1-T},\sqrt T\,v),\quad |v|=1,
 \qquad \mathcal A_d=\frac{e^dd!}{d^d}.
 \tag{15}
\]
The angular integral kills \(i\ne j\), so for every finite \(C\),
\[
 \operatorname{Tr}(P_{N,m}C)
 =\int_0^1q_m(T)\,
   \frac{\mathcal A_de^{-d}}{2\pi i}
   \oint_{|v|=1}\mathcal K_C(Z_d(v,T),\overline{Z_d(v,T)})
                  \frac{dv}{v}\,dT.
 \tag{16}
\]
This identity includes the latitude endpoints by continuity
of the homogeneous kernel. It contains no unknown scalar in
the definition of the integrand.

There are two useful symbol conventions. The normal-coordinate
symbol of S and C is
\[
 f_C(v,T)=\sum_{i,j}C_{ij}\binom dj
                      v^{i-j}T^j(1-T)^{d-j}.
 \tag{17}
\]
The sphere evaluation in (16), multiplied by \(d!/d^d\),
instead has the powers
\(T^{(i+j)/2}(1-T)^{d-(i+j)/2}\).
They are not identified pointwise away from \(T=1/2\).
Both angular averages are exactly
\[
 \overline f_C(T)=\sum_a C_{aa}B_{a,d}(T).
 \tag{18}
\]
Thus (16) and the normal-residue pairing below are exact
presentations of the same finite cut functional.

Now resolve \(C\) as the fixed literal finite network of G.
Each internal edge retains its actual Gaussian integration
and degree-\(d\) projector, including every finite support wall.
For each local matrix, G's Cauchy--Schwarz inequality is
\[
 |\mathcal K_A(Z,\overline W)|
 \le\|A\|_G\,\frac{\|Z\|^d\|W\|^d}{d!}.
 \tag{19}
\]
After applying it at all vertices, each integrated segment
has measure
\[
 d\mu_d(Z)=\frac{\|Z\|^{2d}}{d!}\,d\gamma(Z),
 \qquad \int_{\mathbb C^2}d\mu_d=N.
 \tag{20}
\]
Most importantly, \(\|Z_d(v,T)\|^2=d\) for every real \(T\).
The two boundary evaluation factors and the outside scalar
in (16) therefore cancel exactly:
\[
 \mathcal A_de^{-d}\frac{\|Z_d(v,T)\|^{2d}}{d!}=1.
 \tag{21}
\]

Let \(E\) be the fixed number of integrated segments.
T proves, for the literal balanced signed crossings, pivots,
framing and its allowed compact marking domains,
\(\prod_{\rm vertices}\|A\|_G\le e^{C N}\).
The estimate is uniform on its doubled meridian disk
\(|M-1|\le2\rho/N\), with fixed \(0<\rho<1/8\).
Combining (19)--(21), for every measurable \(B\subset[0,1]\),
\[
 \int_{\{T\in B\}}
       |\text{full finite integrand in (16)}|
 \le N^E e^{CN}\int_Bq_m(T)\,dT .
 \tag{22}
\]
All angular and internal Gaussian variables are integrated on
the left. This is a bound before contraction of the finite
network; it does not follow from the value of \(C_N\).
If the whole modified dimension is present, T's explicit
polynomial bound for it is retained and can be absorbed into
the displayed prefactor.

With \(m=N^2\), (8) and (22) give the actual latitude-tail bound
\[
 \boxed{\displaystyle
 \int_{\{|T-1/2|\ge\varepsilon\}}
       |\text{full finite integrand}|
 \le 2\sqrt{N^2+1}\,N^E
                \exp(CN-4\varepsilon^2N^2).}
 \tag{23}
\]
For every fixed \(\varepsilon>0\) and every \(L>0\), the
right side is at most \(e^{-LN}\) for all sufficiently large
\(N\). The exact unmarked scalar (3) may consequently be
evaluated on the remaining real latitude band with this
absolute error.

The same statement retains each fixed meridian normal.
Apply Cauchy's formula on a radius-\(\rho/N\) circle about
\(|M-1|\le\rho/N\) to the literal integrand, using the doubled
disk in T. Its \(j\)-th derivative has the same integrable
majorant times \(j!(N/\rho)^j\). Fixed clock derivatives use
a slightly larger compact marking domain. These operations
differentiate all pivots, framing and modified factors.
No finite wall or normal row has been dropped.

## 4. The original high-degree normal co-source and current

Let \(\mathcal Q_m(b)=q_m(-b)\). The full Toeplitz map of C
allows arbitrary polynomial degree and gives
\[
 \mathcal T_N(\mathcal Q_m)=N P_{N,m},\qquad
 \frac1N\operatorname{Tr}(\mathcal T_N(\mathcal Q_m)C)
       =\int_0^1q_m(T)\overline f_C(T)\,dT .
 \tag{24}
\]
Its north normal residue is
\[
 \operatorname{Res}_E[\mathcal Q_m(b_N)\nu_{\rm cut}]
                  =-q_m(T)\Omega .
 \tag{25}
\]
The south representative is \(\mathcal Q_m(b_S-1)\), with
C's exact overlap homotopy. The original cut/Haar adapter is
retained before taking the residue. Since \(\deg\mathcal Q_m=2m\),
the full normal pole packet has order \(2m+1\).

For \(m\ge1\), both polynomial endpoint values are zero.
Nevertheless the paired derivative current is in general
nonzero. Integration by parts gives exactly
\[
 \frac1N\operatorname{Tr}(\mathcal T_N(\mathcal Q'_m)C)
 =-\int_0^1q'_m(T)\overline f_C(T)\,dT
 =\int_0^1q_m(T)\overline f'_C(T)\,dT .
 \tag{26}
\]
The two endpoint terms vanish because of the stated original
polynomial, not because every cut current vanishes.
Before pairing, C's product-current identity remains
\[
 d\,\iota_{V_b}[\mathcal Q_m(b_N)f_C\nu_{\rm cut}]
 =[\mathcal Q'_m(b_N)f_C
       -X\mathcal Q_m(b_N)\partial_Tf_C]\nu_{\rm cut}.
 \tag{27}
\]
Equations (26)--(27) retain the kernel derivative and its
change of Bernstein degree. Equation (5) is the separate exact
comparison with the original highest probe, with its marked
commutator. Neither current is suppressed.

Replacing \(\mathcal Q_m\) by a lower-degree polynomial with
the same Toeplitz row is unnecessary and would change this
current presentation: equality of paired rows does not imply
equality of their differentiated rows. In particular it would
not preserve the positivity or localization proved from the
original \(q_m(T)\). The packet in (25) is kept in full even
though \(2m>N-1\).

## 5. What has and has not been removed

This is an exact source-preserving positive localization of
the real cut latitude for the unmarked scalar. It also gives
an absolute estimate for the new marked presentation, with
the exact original-probe defect (5).
The density and each fixed real derivative cost only a
polynomial in \(N\); its normal pole order grows as \(2N^2+1\).

The physical occupations \(a=0,d\) have not been removed.
For example (12) applies to \(w_{m,0}\) and \(w_{m,d}\) as
well: they remain comparable to their binomial values.
Those entries occur inside the interior-latitude coherent
kernel. Thus (23) is not a deletion of physical endpoint
walls or of every collapsed critical stratum.

The proof concerns the original real compact/Gaussian cycle.
It supplies no bound on a fixed complex latitude tube or on
a complexly deformed cycle, no quotient of the surviving
centralizer coordinate, and no lower bound for the remaining
oscillatory integral. It does not identify that integral with
a particular geometric period.

## Complete proof-source pins

* S: notes/research_binomial_cut_framing_density.md,
  SHA256 4bc6efc595fd6d59c0bc572d83495fb779cff230ff1cb9c14429a0b7c6a2a1b0.
* G: notes/research_soft_cut_two_mode_gaussian_source.md,
  SHA256 1f95717e33e0fdcfe6b1cd453a02b4e5e63d83ed578df761a5c8bdd07e990c19.
* T: notes/research_soft_cut_real_gaussian_tails.md,
  SHA256 61d0b6179a1ac15dd6e750b7c6edd8e4e2b386cd2cec02b9fcccb30ad78a7c00.
* J: notes/research_soft_binomial_cut_stationary_source.md,
  SHA256 667cb1eb70b770552de05e6f95f518016852b2c0aecdc874c3dff167fccb3d8b.
* C: notes/centralizer_normal_residue_and_actual_cut_moments.md,
  SHA256 b040461ba07902277ae2964515060e4927322f30c0be81772bed7f2d3da72a1a.

S supplies actual scalarity and the physical Ward transgression;
G supplies the exact finite Gaussian network; T supplies the
literal local norm bounds with the full normalization and
meridian normals; J supplies only the identified principal
stationary-row convention; C supplies the full-degree residue,
clutch and product-current map. All new estimates above are
written proofs. No mathematical programs, tests or builds
were used, and frozen sources and public files are unchanged.
