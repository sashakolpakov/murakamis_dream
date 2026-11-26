# The actual alternating source and its checkerboard Fourier polarization

Private written proof, 19 November 2026. This is a fixed-root theorem for
an actual connected alternating closed-braid diagram. It is not an
assertion that every alternating knot has such a braid presentation.
The original averaged cut, closing pivots, crossing normalizers and
all finite caps remain in the answer.

The new source-specific statement is an exact elimination of all
overclocks, followed by an integer face-coordinate formula and a
finite Fourier polarization of one checkerboard color. Integer
region potentials and finite quadratic Gauss sums are not new
principles. The earlier centered-clock checkerboard adapter concerns
physical clock labels and their determinant development; the charged
angle optimization concerns the original transportation polytope and
an upper bound. Neither is used as a proof of the formula below.
All finite algebra needed here is proved explicitly.

## 1. The literal source and the remaining integer charges

Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad s=x^N,\quad
 S_a=\prod_{j=1}^a2\sin(\pi j/N),\quad f_a=(Q;Q)_a.
 \tag{1}
\]
Empty products are one. Throughout, a real or half-integral power of
q means its displayed exponential, not an independently chosen root.
In particular
\[
 f_a=(-i)^a q^{a(a+1)/2}S_a,\qquad
 S_aS_{d-a}=N.                                             \tag{2}
\]

Let the original braid have b heads and \(c\ge1\) positive or negative
crossing occurrences, with connected alternating closed shadow.
Let \(\sigma_j\in\{1,-1\}\), and \(w=\sum_j\sigma_j\).
The original scalar and its exact external normalization are
\[
 K_N={\chi_N\over N}
  \operatorname{Tr}[(I\otimes g\otimes\cdots\otimes g)W],
 \qquad g_a=(x/s)Q^{-a}.                                   \tag{3}
\]
All framing/dimension factors in \(\chi_N\) and all \(\kappa^{\sigma_j}\)
inside the crossing word are retained. This is precisely G(1), used
only for its original complete word, not for arbitrary inserted marks.

Alternation means that each maximal overbridge has one crossing.
At crossing j name its input-block charges \((u_j,v_j)\) and its
output-block charges \((w_j,z_j)\). Thus
\[
 u_j+v_j+w_j+z_j=d,\qquad h_j=w_j+z_j.                       \tag{4}
\]
The oriented segment containing the underpass at j starts at the
output of an overcrossing \(b(j)\) and ends at the input of an
overcrossing \(a(j)\). Closing adapters may split this segment.
Set
\[
 A_j=u_{a(j)},\quad B_j=z_{b(j)},\quad
 S_j^*=u_j+z_j,\quad L_j=d-S_j^*.
 \tag{5}
\]
The functions a and b are permutations of crossing occurrences.
Here \(S_j^*\) is a charge sum, not a sine factorial.

Define the honest finite integer flow set
\[
 {\cal Q}_N=\{(u,z)\in\mathbb Z_{\ge0}^{2c}:
 u_j+z_j\le d,\quad A_j+B_j=u_j+z_j\text{ for every }j\}.
 \tag{6}
\]
For each original closing adapter on head i, let \(a_i^{\rm cl}\)
be B_j when it lies before the unique underpass on its segment,
and \(d-A_j\) when it lies after that underpass. This rule includes
multiple closing adapters on the same segment. Define
\[
 \tau_{\rm piv}(u,z)=\sum_{i=2}^b a_i^{\rm cl}.
 \tag{7}
\]
The unpivoted first adapter has charge by the same rule but contributes
no summand to (7).

**Exact alternating source theorem.** With precisely the original
normalization in (3),
\[
 \boxed{\begin{split}
 K_N={}&\chi_N\kappa^w(x/s)^{b-1}N^{2c-1}
 \sum_{(u,z)\in{\cal Q}_N}
 q^{\,\frac12\sum_j\sigma_j[
 (z_j-u_j)(B_j-A_j)-d(u_j+z_j)]-2\tau_{\rm piv}}\\
 &\hspace{38mm}\cdot
 \prod_{j=1}^c{1\over S_{u_j}^2S_{z_j}^2S_{L_j}} .
 \end{split}}                                               \tag{8}
\]
Every factorial index is in \([0,d]\). There is no cyclic state
substitution, omitted clock, or discarded endpoint in this formula.

## 2. Proof: local phase, closing charges, and full clock sum

We start from the entire charged bridge identity G(4)--(12), including
its event denominators and closing polynomials. For a one-crossing
bridge, its factorial ratio is one. Its clock phase is
\((-1)^h q^{\sigma h(h+1)}\). The two block gains in G(18) contribute
\(q^{\sigma h(v-z)}\), apart from the propagated port factors.
Since \(h+u+v=d\),
\[
 (-1)^h q^{\sigma h(h+1+v-z)}
       =(-1)^h q^{\sigma h(N-u-z)}
       =q^{-\sigma h(u+z)}.                                \tag{9}
\]
Both signs were used in the last equality; no half-clock was reset.

Consider the long under-segment in (5). Its actual propagated
factor across the underpass is
\[
                    \zeta=x^\sigma Q^{-\sigma h}.
 \tag{10}
\]
The anchor conservation equations on all pieces of the segment
give
\[
                  A+B+v+w=d.                               \tag{11}
\]
Together with (4) this is exactly the equation in (6).
Before the underpass, the closing polynomial's output charge is B:
the preceding anchor equation is \(B+(d-a_i^{\rm cl})=d\).
After the underpass, it is \(B+v+w=d-A\).
Each further adapter on that side repeats the same charge.
This proves (7) and retains the exact factor
\((x/s)^{b-1}Q^{-\tau_{\rm piv}}\) from G(2).

The propagated factor occurs to total exponent \(-B\).
If no closure splits its support, the exponent is \(v+w+A-d=-B\).
If a closure lies after the underpass, it is \(v+w-a_i^{\rm cl}=-B\);
later factors have been reset by their exact closing adapter.
Closures before the underpass do not alter this calculation.
Thus its contribution is \(\zeta^{-B}\) in every case.
Equations (9)--(11) leave
\[
       x^{-\sigma B}q^{\sigma h(B-A)}.                      \tag{12}
\]
The full positive coefficient before summing h is
\[
              {N\over S_uS_zS_{h-z}S_{d-u-h}}.              \tag{13}
\]
This follows either directly from the two sine-binomial blocks and
(2), or from G(4)--(6): their numerators give
\(S_hS_{d-h}=N\). No power of N is assigned to a single
unperformed crossing sum.

Put \(L=d-u-z\), \(h=z+k\), so \(0\le k\le L\). The finite
Gaussian binomial theorem gives
\[
 \begin{split}
 \sum_{k=0}^L {S_L\over S_kS_{L-k}}q^{\sigma k(B-A)}
 &=\prod_{r=0}^{L-1}
        (1+q^{2r-L+1+\sigma(B-A)})\\
 &=\begin{cases}
       f_{d-A}/f_B,&\sigma=1,\\
       f_{d-B}/f_A,&\sigma=-1 .
    \end{cases}                                            \tag{14}
 \end{split}
\]
For the first line, use
\({L\brack k}_Q=q^{k(L-k)}S_L/(S_kS_{L-k})\) in the ordinary
finite product expansion. For the second, \(A+B=d-L\) makes the
positive factors \(1-Q^{B+1+r}\), and the negative factors
\(1-Q^{A+1+r}\), respectively. All indices are between 1 and d.
This also proves (14) at L=0 without division by a vanished factor.

By (2), the two values in (14) have common magnitude
\(N/(S_AS_B)\) and phase \(q^{\sigma L(B-A)/2}\).
Combining (12)--(14) yields the exact local answer
\[
 {N^2\over S_uS_zS_AS_BS_L}
 q^{\,\sigma[(z-u)(B-A)-d(u+z)]/2}.                         \tag{15}
\]
Indeed the ratio of the phase before this simplification to that
displayed in (15) is
\((-1)^Bq^{\sigma NB}=1\).

The independent ranges of h are exhausted by (14). The maps a,b
permute the u and z incidences, so the product of the four first
factorials in (15) is \(\prod_jS_{u_j}^2S_{z_j}^2\).
Each crossing supplies \(N^2\), each closing event has already been
eliminated with its exact charge, and the original source retains
the single \(1/N\) in (3). This proves every factor in (8).

## 3. The exact integer face lattice

Color the regions of the connected planar shadow black and white.
An edge of that shadow lies between one region of each color.
Give it its charge e: it is a u charge at its over-input end or a
z charge at its over-output end, and the same variable is A or B
at its under end. Then (6) says that the sums of the two opposite
port charges agree at every crossing.

There are unique integers \(f_F\), after fixing one black region
\(f_{B_0}=0\), for which
\[
                       e=f_B+f_W                           \tag{16}
\]
on every edge. To prove this rather than count dimensions, put
\(g_B=f_B,\ g_W=-f_W\). On the dual edge from white to black,
prescribe the integral increment e. Its sum around a dual
quadrilateral is \(u+z-A-B=0\). These quadrilaterals are the
two-cells of the dual sphere, including repeated incidences.
Every closed dual walk is an integral sum of their boundaries:
split a walk into simple cycles, and sum the face boundaries in
the disk bounded by each cycle. Path integration therefore defines g
independently of the path, with integer values and fixed base value.
Conversely (16) gives every equation in (6).

The only unconstrained change of the f values is
\(f_B\mapsto f_B+t,\ f_W\mapsto f_W-t\); the fixed black value
removes it. The inequalities in (6) become a literal bounded integer
polytope \({\cal F}_N\) in these fixed face coordinates. Along a
simple dual path there are at most \(\#\text{regions}-1\) edges,
each charge in \([0,d]\), so all face coordinates have absolute
value at most \((\#\text{regions}-1)d\). This is not a quotient
by N. Formula (8) becomes a bijective sum over \({\cal F}_N\).

## 4. The two checkerboard quadratic forms and their signs

At a positive braid crossing take the overpass SW to NE and the
underpass SE to NW. Name the four regions
\((f_0,f_1,f_2,f_3)=(\text{left},\text{bottom},\text{right},\text{top})\).
Then
\[
 u=f_0+f_1,\quad B=f_1+f_2,\quad
 z=f_2+f_3,\quad A=f_3+f_0,
\]
and direct multiplication gives
\[
                (z-u)(B-A)=(f_2-f_0)^2-(f_3-f_1)^2.
 \tag{17}
\]
At a negative braid crossing the overpass is SE to NW. Substitution
of its actual port order and multiplication by \(\sigma=-1\)
reverses the sign on the right. Reversing either oriented strand
exchanges its two ports and reverses \(\sigma\), leaving the product
\(\sigma(z-u)(B-A)\) invariant.

Let \(\eta_j=1\) when the black side is to the left of the incoming
oriented overpass and \(\eta_j=-1\) otherwise. In the positive
convention of (17), left/right black gives \(\eta_j=1\).
The four local sides are: incoming over \(\eta_j\), outgoing
over \(-\eta_j\), incoming under \(-\eta_j\), outgoing under
\(\eta_j\), where a side is encoded by its black/white sign.
Along an alternating edge, these identities force equal \(\eta_j\)
at its two ends. Connectedness therefore gives one sign \(\eta\).
Thus
\[
 \sum_j\sigma_j(z_j-u_j)(B_j-A_j)
       =\eta\{{\cal D}_B(f)-{\cal D}_W(f)\},                 \tag{18}
\]
where each \({\cal D}\) is the sum of squared opposite-region
differences at the crossings, counted with multiplicity.
These are precisely the two checkerboard graph Dirichlet forms.
Loops contribute zero. No assertion of globally flat block gains
was used. Interchanging the two colors makes \(\eta=1\) if desired;
the formulas retain either actual choice.

Both checkerboard graphs are connected: a shadow path gives a path
between its incident black regions using the black edges at the
successive crossings, and the same argument works for white.
After fixing one region of each color, their matrices \(L_B,L_W\)
are positive definite when their size is nonzero: the sum of edge
squares is zero only for a constant on the connected graph.
Let \(X\) be the black coordinates with \(f_{B_0}=0\), choose one
white region, and write the white coordinates as \(t{\bf1}+Y\)
with its chosen coordinate of Y zero. Then
\[
 {\cal D}_B=X^tL_BX,\qquad {\cal D}_W=Y^tL_WY.              \tag{19}
\]
The scalar t is retained, not removed as a second gauge.
The complete exponent in (8) is consequently
\[
 {\,\eta\over2}(X^tL_BX-Y^tL_WY)+\ell_N(X,t,Y),
 \quad
 \ell_N=-{d\over2}\sum_j\sigma_j(u_j+z_j)-2\tau_{\rm piv}.
 \tag{20}
\]
The form \(2\ell_N\) has integral coefficients, including any
constant from a closing charge \(d-A\).

This is a difference of positive quadratic forms, not a positive
state sum. Alternation supplies (18); it does not remove its phase.

## 5. An exact one-color Fourier polarization, including degeneracy

Let \(n=\#\{\text{white regions}\}-1\) and \(m=4N\).
The case n=0 simply omits this transform. For fixed X,t define the
finitely supported amplitude on the integer Y lattice by
\[
 a_{X,t}(Y)=
 {\bf1}_{{\cal F}_N}(X,t,Y)\,
 q^{\ell_N(X,t,Y)}
 \prod_j(S_{u_j}^2S_{z_j}^2S_{L_j})^{-1}.
 \tag{21}
\]
Fold every actual bounded lift, without deleting any, into
\[
 \bar a_{X,t}(\bar Y)=
       \sum_{Y\equiv\bar Y\pmod m}a_{X,t}(Y),
 \qquad \bar Y\in{\cal G}=(\mathbb Z/m)^n.                  \tag{22}
\]
The number of possible lifts is bounded in terms of the fixed
diagram. The quadratic character
\[
 \gamma(Y)=\exp[-2\pi i\,\eta\,Y^tL_WY/m]                  \tag{23}
\]
is genuinely periodic modulo m. Since
\(q^{-\eta Y^tL_WY/2}=\gamma(Y)\), folding gives an exact
identity, not an approximation by a periodic state.

For \(h:{\cal G}\to\mathbb C\), set
\(\widehat h(k)=|{\cal G}|^{-1/2}
\sum_Yh(Y)e^{-2\pi i k\cdot Y/m}\).
Bilinear Fourier inversion proves the original source is
\[
 \boxed{\displaystyle
 K_N=\chi_N\kappa^w(x/s)^{b-1}N^{2c-1}
 \sum_{X,t}e^{2\pi i\eta X^tL_BX/m}
           \sum_{k\in{\cal G}}\widehat\gamma(k)
                              \widehat{\bar a}_{X,t}(-k).}
 \tag{24}
\]
The X,t sum is only over the finite projection of the original
polytope. There is no unrecorded Fourier normalization in (24).
In particular the transformed amplitude is the Fourier transform
of the capped factorial weight (21), not that weight itself.

Here is its exact quadratic support, for every N and every graph.
Put
\[
 {\cal R}=\{r\in{\cal G}:2L_Wr=0\pmod m\}.
 \tag{25}
\]
On \({\cal R}\), \(\gamma\) is a character because its polar
pairing is trivial. Translation of the finite sum gives
\[
 \widehat\gamma(k)=0\quad\hbox{unless}\quad
 e^{-2\pi i\eta r^tL_Wr/m}=e^{2\pi i k\cdot r/m}
                    \quad(r\in{\cal R}).                  \tag{26}
\]
The solutions are one nonempty affine coset of
\({\cal R}^{\perp}=\operatorname{im}(-2\eta L_W)\).
The last equality follows from symmetry, inclusion, and their equal
cardinality \(|{\cal G}|/|{\cal R}|\).
For completeness, any character of a subgroup of a finite abelian
group extends to the group: adjoining one generator at a time
requires choosing a root of its already prescribed power. This
proves nonemptiness without inverting a determinant.

Directly expanding the squared finite sum and setting the difference
of its two variables equal to r shows
\[
 |\widehat\gamma(k)|^2
  =\sum_{r\in{\cal R}}\gamma(r)e^{-2\pi i k\cdot r/m}.
 \tag{27}
\]
It is \(|{\cal R}|\) on (26) and zero otherwise.
In particular the Gauss factor is nonzero exactly there.
Choose any \(k_0\) in that coset. Translation by v gives the precise
phase law
\[
 \widehat\gamma(k_0-2\eta L_Wv)
  =\widehat\gamma(k_0)
       \exp[2\pi i\{\eta v^tL_Wv-k_0\cdot v\}/m].
 \tag{28}
\]
The expression is independent of the representative v modulo the
radical, by (26). The white Dirichlet phase now has the same sign
\(\eta\) as the black quadratic, with its full linear character
and the exact Gauss constant retained.

No parity assumption, coprimality with a graph determinant, or
deletion of a quadratic character on the radical is permitted.
The modulus 4N, rather than N, retains the half-clock exponent
in (20). The phases and all bounded integer lifts in (21)--(28)
are part of this actual polarization.

## 6. The remaining analytic question

Equations (8) and (24) are two exact forms of the original source.
They provide a concrete transform on which a global Legendre
analysis could be attempted. They do not show that
\(\widehat{\bar a}_{X,t}\) is positive, has one contributing phase,
or obeys a strict geometric boundary gap.

Even before transforming, its absolute exponential rate in normalized
charges is the following; u,z in this display denote the corresponding
integer charges divided by N:
\[
 \sum_j\{J(u_j+z_j)-2J(u_j)-2J(z_j)\},\qquad
 J(a)=\int_0^a\log(2\sin\pi v)\,dv.                         \tag{29}
\]
The difference between d/N and 1 costs only \(O(\log N)\) in
the finite factorial estimate, uniformly including all endpoints.
Here is a direct uniform proof. On \([0,1/2]\),
\(\log(2\sin\pi t)-\log t\) is smooth with bounded derivative.
Ordinary integral comparison for \(\sum_{k\le a}\log k\) and
the Riemann sum of that smooth remainder give
\(\log S_a=NJ(a/N)+O(\log(N+1))\) for \(a\le N/2\).
For the other half use (2) and \(J(1-t)=-J(t)\);
moving an argument by \(1/N\) costs \(O(\log(N+1)/N)\), by
integrating the endpoint logarithm. These estimates prove (29)
uniformly on the complete finite polytope.
The single-row negative Hessian determinant is
\[
 2\pi^2\{1+\cot(\pi u)\cot(\pi z)\}
 ={2\pi^2\cos(\pi(u-z))\over\sin(\pi u)\sin(\pi z)}.         \tag{30}
\]
Thus the whole physical triangle is not automatically a concave
angle chart. A Fourier transform of this capped amplitude needs
its own global phase and boundary analysis. The original integer
sum, its cap faces and the affine Gauss sectors in (26) specify
exactly what must be compared.

The theorem concerns the actual alternating closed diagram.
Neither arbitrary braidification nor general mixed Conway filling
preserves that hypothesis automatically. No meridian family,
geometric-cycle coefficient, noncancellation, or new volume limit
is claimed here.

## Complete direct source

The sole complete direct is G,
notes/actual_global_charged_bridge_flow.md, 354 lines, SHA-256
b444e487eab3ec0a56c40b22584837cefcbe374a137b0beeaa185116c2a81d8c.
Its entire source formula, rather than only its local block row, is
used in Sections 1--2. All subsequent lattice and Fourier proofs
are inline.
