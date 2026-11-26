# Every nonzero power at a degree-two vertex

This note proves the full two-boundary asymptotic for one original
degree-two filled vertex at every fixed nonzero signed crossing
power. The missing powers of magnitudes three through thirty-one
are obtained from one contour construction and a finite family of
outward interval certificates. Powers of magnitude one have an
exact reduction to a bare edge. The two boundaries remain open
throughout: the conclusion concerns their entire canonical
polynomial, including all repeated-root normal data.

The result also completes the two-boundary estimate for every
fixed length of a same-sign two-crossing chain. It does not assert
closure under arbitrary adjacent short fillings.

## 1. Statement and conventions

Let \(D=N-1\), \(q=e^{\pi i/N}\), and use the full algebra
\[
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2).
\]
Here \(T_N\) is the usual Chebyshev polynomial. The Newton basis
\(e_0,\ldots,e_D\), original crossing \(R\), and Frobenius trace
\(\phi_N\) have the conventions of
[the original finite source](../papers/circle-tree-volume/finite-bounds.tex).
Put
\[
 K_N(t,u)=\sum_{k=0}^{D}e_k(-2\cos t)e_k(-2\cos u),\qquad
 P_{n,N}(u,v)=
 \phi_N^{(t)}[R^nK_N(t,u)K_N(t,v)].
 \tag{1}
\]
Only the traced variable is reduced in (1). The two remaining
spectral degrees are at most \(D\).

**Theorem 1.** For each fixed integer \(n\ne0\), there are a
holomorphic phase \(S_n\), a holomorphic nonzero amplitude \(A_n\),
and an exact scalar \(\epsilon_{n,N}\) of modulus one such that
\[
 P_{n,N}(u,v)=
 \epsilon_{n,N}N^{-3/2}A_n(u,v)e^{NS_n(u,v)}
                       (1+O_n(N^{-1}))
 \tag{2}
\]
on a fixed complex bidisk about \((0,0)\). The normalized remainder
is holomorphic; each fixed derivative has the same order on
smaller bidisks. Both parities of \(N\) are included. The phase is
separately even and its real Hessian at zero is negative definite.
Writing \(M_n=\Re S_n(0,0)\), there are positive constants
\(c_n,B_n,b_n,C_n'\) and a finite exponent \(a_n\) such that
\[
 |P_{n,N}(u+is,v+it)|
 \le C_n'N^{a_n}
 \exp N\{M_n-c_n(1-\cos u)-c_n(1-\cos v)
                                      +B_n(s^2+t^2)\}
 \tag{3}
\]
for real \(|u|,|v|\le\pi\) and \(|s|,|t|\le b_n\).

All powers are fixed before \(N\to\infty\). No uniform bidisk over
all nonzero integers is asserted here. The phase and scalar
conventions can be chosen as follows:

| Power | Phase in (2) | Exact scalar |
|---|---|---|
| \(n=\sigma=\pm1\) | \(\psi(u,v)-\sigma i(u^2+v^2)/(4\pi)\) | \(1\) |
| \(n=2\sigma\) | the direct phase of the two-index formula | \(1\) |
| \(|n|\ge3\) | the selected original geometric stationary action | \(C_{N,n}=\exp(\pi i nD^2/(4N))\) |

For \(n=2\sigma\), the equivalent geometric phase \(G_{2\sigma}\)
has scalar \(e^{\sigma i\pi N/2}\), since the direct phase is
\(G_{2\sigma}+\sigma i\pi/2\). The phase and its scalar must be
changed together. The first line is an exact boundary-reduction
convention; its marked topological use is described in Section 6.

## 2. The scaled phase for \(3\le n\le31\)

Let
\[
 J(w)=\int_0^w\log(2\sin\pi z)\,dz
\]
start on \(0<w<1\), with the upper and lower continuations
\(J_+\) and \(J_-\) used in
[the factorial continuation estimates](research_uniform_factorial_and_boundary_decay.md).
The canonical Newton phase is
\[
 b(x,t)=\int_0^x
     \Log(2\cos(2\pi z)+2\cos t)\,dz-2J(x).
 \tag{4}
\]
Branches start at \(t=0\), \(0<x<1/2\). At zero angle,
\(b(x,0)=g(x)=J(2x)-4J(x)\).

For positive \(n\), define
\[
 \Psi_n(x,t)=2\{b(x,t)+b(x,0)\}
                        +\frac{int^2}{4\pi}-it.
 \tag{5}
\]
Its selected point is determined by
\[
 \operatorname{arsinh}\tan(t_n/2)
             =i\left(\frac{nt_n}{4}-\frac\pi2\right),
 \qquad
 x_n=\frac1\pi\arctan\cos(t_n/2),
 \tag{6}
\]
on the branches continued from the complete structure.
Write \(x_n=\xi_n+ih_x\), \(t_n=\tau_n-ih_t\), and
\(M_n=\Re\Psi_n(x_n,t_n)\).

The verifier uses the same rational cutoffs for every power:
\[
 \alpha=\frac1{32},\qquad \beta=\frac{15}{32},\qquad
 T=\frac{2\pi}{3}.
 \tag{7}
\]
The root is enclosed before the phase estimates are evaluated.
With \(r=e^{it_n/4}\), its polynomial equation is
\[
 2r^n(r^4-1)-(r^4+1)(r^{2n}+1)=0.
 \tag{8}
\]
A numerical proposal supplies only the center of a rational
disk. On the circle of radius \(2^{-100}\), the verifier compares
the linear Taylor term with the sum of the constant and all
higher Taylor terms, using outward balls. Rouché's theorem
therefore proves that this disk contains exactly one root.

This polynomial root is not accepted without its branch
conditions. The certificate verifies
\[
 0<\tau_n<\frac{2\pi}{n},\quad h_t>0,\quad
 \alpha<\xi_n<\beta,\quad
 0<h_x<\frac{h_t}{2\pi},\quad
 \frac12-\xi_n-\frac{\tau_n}{2\pi}>0.
 \tag{9}
\]
Equation (8) implies
\(\tan(t_n/2)=-i\cos(nt_n/4)\).
The number \(w=i(nt_n/4-\pi/2)\) has positive real part and
imaginary part strictly between \(-\pi/2\) and zero. Thus
\(\operatorname{arsinh}(\sinh w)=w\) on the principal branch,
which proves the first equation in (6), not merely its
exponential. The chosen arctangent proves the wire equation.
The positive factorial bulk margin in (9) fixes its logarithmic
branch. More explicitly, the exponentiated wire and trace
equations restrict their continued logarithmic derivatives
to discrete integer multiples of \(4\pi i\) and \(i\),
respectively. The verifier bounds each derivative in modulus
by \(1/100\), so the only possible value is zero.
[The certificate proof](research_internal_degree_two_contour_certificates.md),
Section 1, gives these branch calculations in full.

For clarity, the analytic normalization agrees with the complete
branch along the whole cone path. Write \(t=2a-2ib\).
The positive geometric branch satisfies
\[
 \sin a=\cosh b\,\tanh(nb/2),\qquad
 na+2\arctan(\sinh b/\cos a)=\pi\lambda,\quad 0<\lambda\le1.
 \tag{10}
\]
Both \(a\) and \(b\) increase with \(\lambda\). Since \(n>2\),
\(\sin a>\sinh b\), and therefore
\(|\cos(a-ib)|<1\). It follows that
\(0<\Re x<1/4\). Also \(a<\pi/4\): for \(n\ge4\) this
follows from \(na<\pi\). For \(n=3\), at \(a=\pi/4\) the
first equation forces \(b>3/10\), because
\(\cosh(3/10)\tanh(9/20)<(21/20)(9/20)<1/\sqrt2\).
It then gives
\(\sinh b/\cos a>(3/10)\sqrt2>\sqrt2-1=\tan(\pi/8)\),
so \(\arctan(\sinh b/\cos a)>\pi/8\), making the second
left side exceed \(\pi\). Thus
\[
        \Re(1/2-x\pm t/(2\pi))>0
\]
on the selected path. The local action in (5) continues from the
same complete factorial branch, with no added logarithmic period.

## 3. What the certificates prove

The reusable
[scaled contour lifting theorem](research_scaled_wire_contour_lifting.md)
lists six groups of inequalities. Its exact trace-first
decomposition requires nineteen two-real-variable surfaces at
degree two. The script
[certify_internal_degree_two_contours.py](../experiments/certify_internal_degree_two_contours.py)
checks precisely those surfaces, retaining the branch of each
factorial on each side of a cut. It proves:

| Surface | Certified gap below \(M_n\) |
|---|---|
| upper wire, lower trace, outside the selected rectangle | \(10^{-7}\) |
| upper wire with negative real trace angle | \(1/(100n^2)\) |
| lower wire, including its penalty \(4\pi h_x\) | \(1/(100n^3)\) |
| angular cutoff connectors | \(1/1000\) |
| wire endpoints on the bottom angular contour | \(1/1000\) |
| nested wire endpoints on angular connectors | \(1/1000\) |

The local rectangle has a certified negative definite real
Hessian. Exact stationarity and strict concavity give its unique
maximum. Each accepted box in the complement has a strict upper
bound; the saved boxes cover every indicated domain. The nested
endpoint bound retains the product of the two independent height
parameters, rather than checking only their corners.

Every wire correction is multiplied by the degree in the scaled
phase. In particular, the lower-wire penalty in (5) is
\(2(2\pi h_x)\). The unit angular charge in \(-it\) is shared
and is never multiplied again. For the original three-variable
phase
\[
 \mathcal F_n(x_1,x_2,t;u,v)=
 b(x_1,t)+b(x_1,u)+b(x_2,t)+b(x_2,v)
                              +\frac{int^2}{4\pi}-it,
 \tag{11}
\]
at \(u=v=0\) one has the exact identity
\[
 \Re\mathcal F_n-p_1-p_2
 =\tfrac12\{\Re\Psi_n(x_1,t)-2p_1\}
  +\tfrac12\{\Re\Psi_n(x_2,t)-2p_2\}.
 \tag{12}
\]
Consequently a bad wire with a scaled gap \(\delta\) gives a
gap at least \(\delta/2\) in the actual source. On an angular
connector every wire has the corresponding gap.

This argument uses the trace-first ordering. It does not
deform all heights simultaneously over the interior angular
interval: on that different deformation the regular wire
phase can exceed \(M_n\), and (12) alone would not suffice.
The exact ordering, rational alias factors, endpoint
orientations and the small-height collar are proved in
Sections 4--5 of the lifting theorem.

The [complete record](../repro/results/research-internal-degree-two-contours.json)
contains all twenty-nine powers and \(29\cdot19=551\) surface
domains. These are outward-arithmetic proofs of the stated
limiting-phase inequalities. The finite-source passage uses
the additional arguments below; it is not inferred from
numerical convergence.

## 4. The finite factorial domains and all discarded terms

The exact Newton interpolation is
\[
 B_N(x,t)=
 \frac{N}
 {G_N(N(1/2-x+t/(2\pi))-1/2)
  G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{13}
\]
It equals \(e_k(-2\cos t)\) at \(x=k/N\). The numerator is
exactly \(N\), by the factorial reflection identity; it has
not been replaced by a leading term.

On all trace-first wire rectangles,
\(\alpha\le\Re x\le\beta\) and \(|\Re t|\le T\). Hence
\[
 -\frac{29}{96}\le
     \Re(1/2-x\pm t/(2\pi))
                      \le\frac{77}{96}.
 \tag{14}
\]
For a real free angle \(|u|\le\pi\), the corresponding interval
is
\[
 -\frac{15}{32}\le
     \Re(1/2-x\pm u/(2\pi))
                      \le\frac{31}{32}.
 \tag{15}
\]
There is thus a fixed margin from the endpoints \(-1,1\)
required by the uniform reciprocal-factorial bound. The same
is true after the actual half-grid endpoints move by
\(O(N^{-1})\). One may use, for example, an endpoint margin
\(1/64\) for all sufficiently large levels. The imaginary
heights are bounded because only finitely many powers occur
here. The \(G_N(Nx)\) denominator remains in a compact bulk
strip.

The reciprocal factors in (13) are holomorphic on these
rectangles. When an argument crosses a nonpositive integral
factorial value the reciprocal can vanish; it does not create
a pole. The upper estimate across the cut retains the two
terms of the reflection cosine. At the bottom angular
contour, (9) puts the \(+t\) argument below its cut and the
\(-t\) argument above it. The same holds at every positive
depth of an angular connector and at each of its nested
wire endpoints. At depth zero the two real upper exponents
agree. These are exactly the branches used in the verifier.
The uniform estimates include moving zeros and their
intersections.

Near the selected saddle, (9) makes both real factorial
arguments positive. The full bulk expansion is therefore
\[
 B_N(x,t)B_N(x,u)=
 \frac{e^{N\{b(x,t)+b(x,u)\}}}{4N^2\sin^2(\pi x)}
                              (1+O(N^{-1})),
 \tag{16}
\]
with a holomorphic remainder and uniform fixed derivatives.
The shifts \(-1/2\) in (13) produce the displayed density;
they are retained in this expansion.

There are two separate discarded regions. First, the original
full Hermite norm bounds give the rate \(M_\infty=4G/\pi\)
for an unrestricted wire and \(2g(\alpha)\) for a wire
outside \([\alpha,\beta]\), including every high index.
The certificate proves
\[
          M_n-M_\infty-2g(1/32)>\frac14.
 \tag{17}
\]
This bounds the original omitted terms before taking the
trace, including all first normals. Second,
[the all-degree outer-angle estimate](research_all_degree_outer_angle_gap.md)
applies to every retained wire subset and all real parent
angles. It gives rate less than \(8/5\) for the original
trace at \(|t|\ge2\pi/3\). The certificate proves \(M_n>9/5\).
Thus the discarded angular region also has a fixed gap.
Both estimates allow the polynomial costs of the fixed
crossing power and the exact Hermite trace.

At the actual angular cutoff \(T_N=T+O(N^{-1})\), use
\(T_N\ge T\). The outer estimate still applies. The compact
contour inequalities persist after decreasing their gaps.
At a moving factorial zero, the uniform primitive modulus
is \(O(\varepsilon|\log\varepsilon|)\); a half-step changes
the exponent by \(O(\log N)\), absorbed in a polynomial
prefactor. In the collar of angular height \(0\le s\le1/N\),
leave the retained product unexpanded and use its real
outer-angle bound and polynomial continuation. This avoids
singular separate wire weights as their heights tend to zero.

All these are estimates for the original finite source.
Together with the nineteen inequalities, they verify every
hypothesis of the lifting theorem.

## 5. Leading coefficient and the whole-boundary bound

Let \((x_1(u,v),x_2(u,v),t(u,v))\) be the holomorphic critical
point of (11) through \((x_n,x_n,t_n)\), and set
\[
 S_n(u,v)=\mathcal F_n(x_1(u,v),x_2(u,v),t(u,v);u,v).
 \tag{18}
\]
Let \(H_n\) be its Hessian in the three internal variables.
The result of the exact contour construction is (2) with
\(\epsilon_{n,N}=C_{N,n}\) and
\[
 A_n(u,v)=
 \frac{i(2\pi)^{3/2}}{16\pi}
 \frac{\sin t(u,v)}
 {\sin^2(\pi x_1(u,v))\sin^2(\pi x_2(u,v))
                              \sqrt{\det(-H_n(u,v))}}.
 \tag{19}
\]
The square root is fixed by the convergent Gaussian on the
selected horizontal contour. The trace contributes \(N^2\),
the two wire sums \(N^2\), their two Newton products \(N^{-4}\),
and the three-dimensional Gaussian \(N^{-3/2}\). There is
no extra factor of two from a wire sum or a level parity.

At zero boundary, if
\(a=F_{xx}\), \(b=F_{xt}\),
\(c=2F_{tt}+in/(2\pi)\), where \(F=b(x,t)+b(x,0)\), then
\[
 H_n=\begin{pmatrix}a&0&b\\0&a&b\\b&b&c\end{pmatrix},
 \qquad
 \det(-H_n)=\frac{-a}{2}\det(-\Psi_n'').
 \tag{20}
\]
The certified negative real Hessian of \(\Psi_n\) gives a
negative real Hessian of \(H_n\), including its transverse
wire direction. The sine factors and \(\sin t_n\) are
nonzero. This proves that (19) is nonzero and remains so
on a sufficiently small bidisk.

Separate evenness gives zero first variations of the internal
critical coordinates at \(u=v=0\). Therefore
\[
 S_n''(0,0)=-\frac{\tan(\pi x_n)}{2\pi}I_2
           =-\frac{\cos(t_n/2)}{2\pi}I_2,
 \tag{21}
\]
whose real part is negative definite.

For all real parent angles, the exact factorial estimate on
every retained contour has the additional loss
\[
 -\gamma_n(1-\cos u)-\gamma_n(1-\cos v),\qquad
 \gamma_n=\min_{\alpha\le\xi\le\beta}
       \frac{\sin(2\pi\xi)}{4\pi\cosh^2(\pi h_x)}>0.
 \tag{22}
\]
This applies at either wire height and at all intermediate
heights. The already discarded original terms have a
fixed gap uniformly on the real torus; reducing the angular
coefficient absorbs them too. Thus the full polynomial,
not just its selected contribution, satisfies a strict
real angular bound. Near zero, its local nonzero packet
and (21) give the quadratic complex-angle bound. Away
from zero, separate degree at most \(D\) and a finite
product-interval Chebyshev continuation preserve the
strict gap on a thin fixed product strip. These give (3).

This proves Theorem 1 for \(3\le n\le31\).
For \(n\le-3\), use the conjugate holomorphic germs
\[
 S_{-n}(u,v)=\overline{S_n(\bar u,\bar v)},\qquad
 A_{-n}(u,v)=\overline{A_n(\bar u,\bar v)}.
 \tag{23}
\]
The original polynomials have exactly this coefficient
conjugation, including all normal terms.

For \(|n|\ge32\), degree two satisfies
\(4+n^2\ge\max(1024,256)\), so
[the degree-and-power theorem](research_high_degree_short_internal_vertex.md)
already proves (2)--(3), with the same geometric phase
normalization and scalar \(C_{N,n}\).
For \(n=\pm2\), use
[the full two-boundary theorem](research_degree_two_power_two_boundary_theorem.md)
and its
[proved geometric phase comparison](research_degree_two_power_two_geometric_phase.md).

## 6. Powers one and minus one, and the marked geometry

Let \(M\) be the original multiplication-by-\(R\) matrix,
\(J\) Newton reversal, and \(\kappa_N=q^{D^2/2}\). The
coefficient matrix of \(K_N\) is \(I\), and that of
\(P_{\sigma,N}\) is \(JM^\sigma\). The full-algebra braid
identity and Frobenius transpose relation imply
\[
 \begin{split}
 JM^\sigma
 &=\kappa_N^\sigma M^{-\sigma}JM^{-\sigma}J\\
 &=\kappa_N^\sigma M^{-\sigma}(M^{-\sigma})^T .
 \end{split}
 \tag{24}
\]
Thus, in the canonical tensor algebra,
\[
 P_{\sigma,N}
   =\kappa_N^\sigma
      (R^{-\sigma}\otimes R^{-\sigma})K_N.
 \tag{25}
\]
The two-boundary multiplication theorem in
[the internal chain note](research_internal_two_crossing_chain.md),
Proposition 2, applies to the proved full bare-edge packet.
It preserves mixed normals as well as the separate first
normals. It gives the first line of the table, with the
bare-edge amplitude \(a_e(u,v)\), because
\[
              \kappa_N^\sigma C_{N,-\sigma}^{\,2}=1.
 \tag{26}
\]
In particular \(A_{\sigma}(0,0)=1/4\) and the real boundary
Hessian is \(-I_2/(2\pi)\). This finishes the analytic
theorem for every nonzero integer.

For \(|n|\ge3\), the phase (18) equals the stationary
action of the original two positive edge blocks. The wire
critical equations eliminate \(x_1,x_2\) to give
\[
 \operatorname{stat}_t\left[
      \psi(t,u)+\psi(t,v)+\frac{int^2}{4\pi}-it\right].
 \tag{27}
\]
The branch comparison in Section 2 fixes its constant.
[The isolated-vertex geometry](research_isolated_internal_vertex_geometry.md)
then supplies the original positive shapes, full primitive
periods, and the cone path from the complete structure.
Schläfli's formula gives absolute volume \(2\pi M_n\);
the remaining cusps and their marked deformations are
retained. For \(n=\pm2\) the same statement follows from
the separate phase comparison already cited.

For \(n=\sigma\), the topological counterpart of (25) is
[the marked degree-two move](research_marked_degree_two_tangle_moves.md),
Proposition 1. In its left-stack convention,
\[
 T(R^\sigma T(F))
       \simeq R^{-\sigma}T(R^{-\sigma}K(F)),
 \tag{28}
\]
where \(K\) is the actual proper half-turn, carrying every
mark and ribbon of the arbitrary attached tangle \(F\).
Both neighboring powers shift by \(-\sigma\). In the
right-stack convention the corresponding displayed
identity has no half-turn. Use the convention appropriate
to the original attachment; (24) does not erase this
physical rotation. The remaining bare-edge geometry,
with those two boundary shifts, gives the stated phase
and its absolute volume.

There is also a direct comparison that keeps the original
filled core and both original boundary labels. The
[unit-power geometric lemma](research_degree_two_unit_power_geometry.md)
proves
\[
 dG_{2,\sigma}
   =d\{\psi(u,v)-\sigma i(u^2+v^2)/(4\pi)\},\qquad
 \Re G_{2,\sigma}(0,0)=\psi(0,0).
\]
It uses the original critical angle with
\(\cos(t/2)=\cos(u/2)\cos(v/2)
+i\sigma\sqrt{1-\sin^2(u/2)\sin^2(v/2)}\).
Thus the source phase has the original primitive
peripheral derivatives and real volume normalization
without replacing the geometric piece by an unmarked edge.

## 7. Reproduction and consequence for chains

The contour verifier depends on the existing terminal
primitive-enclosure and rational-box engine. Its new data
are the degree-two algebraic root, the scaled phase and
wire penalties, and the nineteen required surfaces.
The command is

~~~sh
python3 experiments/certify_internal_degree_two_contours.py \
  --powers 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 \
           18 19 20 21 22 23 24 25 26 27 28 29 30 31 \
  --precision 180 \
  --output repro/results/research-internal-degree-two-contours.json
~~~

Each record includes the exact integer polynomial, rational
root center and radius, Rouché comparison, local Hessian
cover, and every accepted rational box. A failed inequality
or exhausted subdivision budget aborts without asserting
the theorem. Outward ball arithmetic and subdivision are
standard tools; see Johansson,
[Arb: efficient arbitrary-precision midpoint-radius interval arithmetic](https://doi.org/10.1109/TC.2017.2690633)
and the [Arb documentation](https://flintlib.org/doc/arb.html).
The source-specific ingredients are the phase, original
contour identities and their finite error estimates.

For a chain of \(k\ge1\) internal vertices of equal power
\(2\sigma\), the exact reduction is to the internal power
\(-\sigma(k+1)\), with a boundary crossing on each side.
This power is now covered for every fixed \(k\). Therefore
equation (14) of
[the two-boundary chain theorem](research_internal_two_crossing_chain.md)
and its full Gaussian strip hold for every fixed positive
length. All physical rotations and boundary shifts in
that note remain part of the statement. The result fills
this entire family of short chains; it does not provide
a contour theorem for arbitrary mixed short words.
