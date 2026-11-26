# The factorial phase of the canonical free-boundary Newton interpolation

The exact circle-averaging formula for original Newton wires uses a
finite cardinal interpolation at a free boundary. Its identification
with the sine-factorial interpolation was previously available only
in the physical quotient. This note proves a uniform exponentially
small difference near the complete free boundary, for every fixed
compact set of wire indices in \(0<\Re x<1/2\).

The estimate concerns the whole canonical boundary polynomial, not
just its values at the distinct physical roots. It controls the
coherent sum defining that polynomial and includes both parities
and all fixed boundary and index derivatives. It supplies a
boundary factor in an exact all-wire integral. It does not select
the dominant cycle of the remaining angle contractions.

## 1. The two actual interpolations

Put \(D=N-1\), \(\eta=(-1)^D\), and
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 e_j(z)=\frac{\prod_{k=0}^{j-1}
                  (2\cos((2k+1)\pi/N)-z)}
                 {\prod_{k=1}^j4\sin^2(\pi k/N)}.
 \tag{1}
\]
The standard Chebyshev convention is used. Define
\[
 s_N(x)=\frac{\sin(\pi Nx)}{N\sin(\pi x)},\qquad
 \widetilde B_N(x,z)=\sum_{j=0}^{D}s_N(x-j/N)e_j(z),
 \tag{2}
\]
with the removable values in \(s_N\) understood. The polynomial
\(\widetilde B_N\) has degree at most \(D\) in \(z\).
Its exact factorial counterpart is
\[
 B_N(x,u)=
 \frac{N}
 {G_N(N(1/2-x+u/(2\pi))-1/2)
  G_N(N(1/2-x-u/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{3}
\]
Here \(G_N\) is the original canonical sine factorial. These are
precisely the interpolations in
[the finite Fourier-band theorem](research_newton_interpolation_finite_fourier_band.md).
At \(x=j/N\), both are the original \(e_j(-2\cos u)\).
For arbitrary \(x\), that theorem proves
\[
 [\,\widetilde B_N(x,z)\,]=[\,B_N(x,u)\,],
                 \qquad z=-2\cos u,
                 \quad\text{in }\mathbb C[z]/P_N(z).
 \tag{4}
\]
Thus (4) includes the first normal at every double root.
It is not an ordinary equality away from those roots.

Fix
\[
 \mathcal X=\{x:\alpha\le\Re x\le\beta,\ |\Im x|\le H\},
                \qquad 0<\alpha<\beta<1/2,\quad H<\infty.
 \tag{5}
\]
Choose a slightly larger closed rectangle of the same kind
when derivatives on \(\mathcal X\) are required. On a small
common disk in \(u\), put
\[
\begin{split}
 b(x,u)&=-J(1/2-x+u/(2\pi))
         -J(1/2-x-u/(2\pi))-2J(x),\\
 J'(w)&=\log(2\sin\pi w),\qquad J(0)=0.
\end{split}
 \tag{6}
\]
All arguments in (6) have real part strictly between zero and
one on a sufficiently small disk. Their branches are continued
from \(0<w<1\). In particular \(b(x,0)\) is holomorphic on
an open neighborhood of \(\mathcal X\).

**Theorem 1.** There are \(r,\delta,c,h>0\) and finite constants
\(C,A,B\), depending only on (5), such that for every integer
level \(N\ge2\),
\[
 \sup_{-\pi\le u\le\pi}
 \left|\widetilde B_N(x,-2\cos u)-B_N(x,u)\right|
       \le C N^A e^{N(\Re b(x,0)-\delta)}
                       \qquad(x\in\mathcal X).
 \tag{7}
\]
On the complex disk \(|u|\le r\) there is also a fixed
exponential gap, possibly smaller than that in (7). In
particular, uniformly on a neighborhood of a smaller
closed product domain,
\[
 \widetilde B_N(x,-2\cos u)
 =B_N(x,u)\bigl(1+O(e^{-\delta N})\bigr)
 =\frac{e^{Nb(x,u)}}{2N\sin(\pi x)}
                         (1+O(N^{-1})).
 \tag{8}
\]
The constants called \(\delta\) in (7)--(8) can be replaced
by their positive minimum. The normalized errors are
holomorphic; every fixed mixed derivative in \(x,u\) has
the corresponding estimate on smaller product domains.
The exact canonical polynomial also satisfies
\[
 |\widetilde B_N(x,-2\cos(a+iv))|
 \le C N^A
 e^{N\{\Re b(x,0)-c(1-\cos a)+Bv^2\}},
       \qquad |a|\le\pi,\quad |v|\le h.
 \tag{9}
\]
No amplitude zero or parity factor is introduced in (8).

## 2. A uniform angular strip for the factorial interpolation

The reciprocal midpoint estimate in
[the uniform factorial theorem](research_uniform_factorial_and_boundary_decay.md)
applies on (5), throughout \(-\pi\le u\le\pi\). It gives
\[
 |B_N(x,u)|\le\frac{C}{N}
        e^{N\{\Re b(x,0)-c_0(1-\cos u)\}},
 \qquad
 c_0=\min_{x=\xi+i h_x\in\mathcal X}
       \frac{\sin(2\pi\xi)}{4\pi\cosh^2(\pi h_x)}>0.
 \tag{10}
\]
This is an estimate of the exact function. It retains the
reciprocal-factorial zeros crossed by its shifted arguments.

We need a strip estimate before doing Fourier projection.
Here that estimate does not require a polynomial-degree
argument. For \(u=a+iv\), the real parts of the two shifted
arguments divided by \(N\) range from \(-\beta\) to
\(1-\alpha\) when \(|a|\le\pi\). They therefore remain
strictly below one and above minus one. The reciprocal
factorials in (3) are holomorphic there, including at their
zeros. The same remains true on a slightly larger real
window and on a fixed small complex strip.

The real upper exponent \(\mathfrak b(x,u)\) in equation
(5) of the uniform factorial theorem is continuous on
this compact set. Its side values agree at the negative
real cut, and \(w\log w\) is continuous at zero. Thus,
away from any fixed neighborhood of \(a=0\), (10) keeps
at least half its strict angular loss after decreasing
the strip width.

Near zero the branches in (6) are holomorphic and
\[
 b_u(x,0)=0,\qquad b_{uu}(x,0)
                    =-\frac{\tan(\pi x)}{2\pi}.
 \tag{11}
\]
For \(x=\xi+i h_x\),
\[
 \Re\tan(\pi x)=
       \frac{\sin(2\pi\xi)}
            {\cosh(2\pi h_x)+\cos(2\pi\xi)}>0.
 \tag{12}
\]
It has a positive minimum on (5). Uniform Taylor bounds
and completion of the mixed real-imaginary quadratic
term now give
\(\Re(b(x,a+iv)-b(x,0))\le-c_1a^2+C_1v^2\)
on a common neighborhood. Combine this with the
preceding far-angle bound. For fixed \(c_2,h_2>0\)
and \(C_2<\infty\),
\[
 |B_N(x,a+iv)|\le C N^A
 e^{N\{\Re b(x,0)-c_2(1-\cos a)+C_2v^2\}},
          \quad |a|\le\pi,\ |v|\le h_2.
 \tag{13}
\]
The same estimates on disks of radius \(1/(10N)\)
bound each fixed angular derivative with only an
additional power of \(N\). At the moving cutoff points
below, these disks stay strictly inside the real window.
At the finitely many smaller levels constants may be
increased. All choices are uniform in \(x\).

## 3. Full Hermite projection of the factorial function

For clarity we give the part of the projection argument
which controls cancellation. Choose an even smooth cutoff
\(\chi_N\), equal to one on
\[
 |u|\le a_N=\pi-\frac{3\pi}{4N}
\]
and zero on \(|u|\ge\pi-\pi/(4N)\), with
\(|\chi_N^{(j)}|\le C_jN^j\). Extend
\[
                   f_{N,x}(u)=\chi_N(u)B_N(x,u)
 \tag{14}
\]
periodically. The last physical angle is \(\pi-\pi/N<a_N\).
Thus \(f_{N,x}\) and \(B_N(x,\cdot)\) agree in value and
first angular derivative at every physical angle. At the
odd simple root zero the derivative vanishes by evenness
and imposes no additional normal condition.

Write \(\widehat f_\ell\) for the Fourier coefficients
of (14). Its full physical Hermite interpolant is exactly
\(\widetilde B_N(x,-2\cos u)\), by (4). If its even Fourier
coefficients are \(b_m\), the exact folding formula is
\[
 b_m=\sum_{k\in\mathbb Z}(k+1)\eta^k\widehat f_{m+kN},
                \quad 1\le m<N,\qquad
 b_0=\sum_{k\in\mathbb Z}\eta^k\widehat f_{kN}.
 \tag{15}
\]
The term \(k=-1\) in the first sum is zero. Consequently
\[
 \|\widetilde B_N(x,-2\cos\cdot)-f_{N,x}\|_\infty
 \le C\sum_{|\ell|\ge N}
                  (1+|\ell|/N)|\widehat f_\ell|.
 \tag{16}
\]
This is the full Hermite formula, proved in
[the boundary-multiplication theorem, Section 2](research_boundary_crossing_packet_preservation.md).
It keeps every alias and first normal; value interpolation
alone would not give (16).

Choose \(h_3<h_2/4\) with
\(C_2h_3\le1/4\) and \(C_2h_3^2\le c_2/8\).
Integrate the Fourier coefficient four times by parts
before moving the remaining analytic central integral
to height \(-\operatorname{sgn}(\ell)h_3\).
The derivatives of the cutoff occur only in endpoint
layers with a fixed angular gap. Both vertical sides
of the central rectangle also have that gap by (13).
The Fourier factor decreases on those sides. Thus,
for \(|\ell|\ge N\), with \(M(x)=\Re b(x,0)\),
\[
 |\widehat f_\ell|
 \le\frac{C N^{A+4}}{|\ell|^4}
 \left[
 e^{N(M(x)+C_2h_3^2)-|\ell|h_3}
            +e^{N(M(x)-c_2/4)}\right].
 \tag{17}
\]
All vertical currents have been bounded in the second
term, rather than omitted. Summing with the weight in
(16) gives
\[
 \sum_{|\ell|\ge N}(1+|\ell|/N)|\widehat f_\ell|
 \le C N^{A+1}e^{N(M(x)-\delta_0)},\qquad
                 \delta_0=\min(h_3/2,c_2/8)>0.
 \tag{18}
\]
The difference between \(f_{N,x}\) and \(B_N(x,\cdot)\)
is confined to endpoint layers and has a still fixed
exponential gap by (10). This proves (7).

The cutoff is solely an estimate for the Fourier tail.
The polynomial being estimated remains exactly (2);
the smooth function is never analytically continued.

## 4. Local complex comparison and the nonzero amplitude

Let \(E_N(x,u)=\widetilde B_N(x,-2\cos u)-B_N(x,u)\).
It is holomorphic on a fixed neighborhood of the real
window. From (7), every Fourier coefficient of the
canonical polynomial is bounded by
\(CN^A e^{NM(x)}\). Its degree \(D\) therefore gives
\[
 |\widetilde B_N(x,-2\cos(a+iv))|
                  \le CN^{A+1}e^{N(M(x)+|v|)}.
 \tag{19}
\]
Fix a half-disk \(|u|<a<h_2/2\), and set
\(C_a=\max(a,C_2a^2)\). On its curved boundary,
(13) and (19) bound \(E_N\) by a polynomial times
\(e^{N(M(x)+C_a)}\). On its real diameter, (7)
has exponent \(M(x)-\delta_0\).

The harmonic measure of the curved boundary at \(u\)
is at most \(16|\Im u|/(3\pi a)\) for \(|u|\le a/2\).
The two-constants inequality therefore supplies a
common \(r>0\) on which
\[
 |E_N(x,u)|\le CN^{A'}e^{N(M(x)-\delta_0/2)}.
 \tag{20}
\]
For example any
\[
 r\le\min\left\{a/2,\
       \frac{3\pi a\delta_0}{32(\delta_0+C_a)}\right\}
 \tag{21}
\]
works. This argument uses the analytic \(E_N\), not
the cutoff in (14).

The ordinary bulk factorial expansion in (3) is
\[
 B_N(x,u)=\frac{1}{2N\sin(\pi x)}
             e^{Nb(x,u)}(1+O(N^{-1})).
 \tag{22}
\]
The two midpoint factorials each contribute \(\sqrt N\);
the squared \(G_N(Nx)\) contributes
\(2N\sin(\pi x)\); the numerator is \(N\).
This checks the full leading power and coefficient.
The sine is bounded away from zero on (5).
Shrink \(r\) so
\(\Re b(x,u)\ge M(x)-\delta_0/8\).
Equation (20) is then exponentially smaller than (22),
proving (8), with its nonzero amplitude.

Apply the proof first on a slightly larger wire rectangle
and boundary disk. Cauchy's estimates on the resulting
holomorphic normalized error give every fixed mixed
derivative assertion. In particular this comparison
preserves the derivative data needed by a subsequent
full trace at a free boundary.

Finally (7), (10) give a real angular loss for the
canonical polynomial, with any sufficiently small
\(c\le\min(c_0,\delta_0/2)\). Near zero, (8),
(11)--(12) extend it with a quadratic imaginary cost.
Away from zero, the degree-\(D\) polynomial bound on
a fixed spectral interval and its Chebyshev continuation
retain half the real gap on a fixed strip. This is
exactly the local/far strip argument in Section 5 of
the boundary-multiplication theorem, with the uniform
parameters just established. It proves (9).

## 5. Consequence for an exact original-source integral

Use the cardinal interpolation at both ends of every
original wire, including the free ends. The exact
[all-wire circle identity](research_internal_wire_exact_circle_averaging.md)
then represents its full boundary polynomial by a
product of complete index periods. The two factors
at each wire have combined Fourier band
\([-N+1,N-1]\); all internal-index aliases and side
currents cancel exactly. Crossing powers and all
physical traces remain the original ones.

On a compact part of that index cycle where every
free-end index satisfies (5), its boundary factors
may now use (3) and (22) on a fixed complete-boundary
polydisk, with an exponentially small relative error.
There are only finitely many free factors in a fixed
network. Their product therefore has the same
property, with all mixed free-boundary derivatives.
At internal ends the identification with the
factorial class is already exact by (4).

This is a pointwise comparison on the specified
compact part of the exact cycle. After integration,
its absolute error is bounded by an exponentially
small factor times the integral of the absolute
factorial integrand on that part. A relative estimate
for a possibly cancelling whole period still needs
a lower bound for that period. Nor does this note
control index regions with \(\Re x\ge1/2\), or move
the physical-angle cycle to a positive geometric
one. Those are the remaining adjacent-component
tasks. The new conclusion is that a free boundary
does not itself prevent using the actual factorial
phase on the low-index part of the exact circle
representation.

## 6. Why the same concentrated class cannot cover a full index period

The low-index restriction cannot be removed merely by using the same
complete-boundary rate on the rest of the exact wire circle. There
is an exact Fourier obstruction at \(x=3/4\).

The coefficient of \(e^{iDu}\) in \(e_D(-2\cos u)\) is \(1/N^2\).
Lower Newton polynomials have smaller Fourier degree. Hence the
highest coefficient of the exact cardinal polynomial is
\[
 [e^{iDu}]\widetilde B_N(x,-2\cos u)
       =\frac{s_N(x-D/N)}{N^2}
       =\frac{(-1)^D\sin(\pi Nx)}
                    {N^3\sin(\pi(x-D/N))}.
 \tag{23}
\]
For \(x=3/4\) and \(N=4m+2\), its magnitude is at least \(N^{-3}\).
Fourier extraction on the real period therefore gives
\[
 \sup_{u\in[-\pi,\pi]}|\widetilde B_N(3/4,-2\cos u)|
                                      \ge N^{-3}.
 \tag{24}
\]
On the other hand, the real factorial phase at the complete
boundary is
\[
 \mathfrak b(3/4,0)=4J(1/4)<0.
 \tag{25}
\]
Indeed \(\Re J_{\rm side}(-1/4)=-J(1/4)\) and
\(J(3/4)=-J(1/4)\). Also \(J(1/4)<0\), for instance from
the positive integral of \(\log\cot t\) on \((0,\pi/4)\).
Equations (24)--(25) exclude every global bound of the form
(9) centered at this factorial complete-boundary rate, even
with an arbitrary fixed polynomial prefactor and with the
angular loss removed entirely.

This obstruction uses the highest coefficient of the original
canonical polynomial, including its exact \(N^{-2}\) Newton
normalization. It does not prove a failure of a knot volume
limit or of a more suitable cycle. It does prove that an
argument which extends the low-index concentrated boundary
class around the entire index circle loses actual Fourier
content. High-index sectors require separate estimates or
a source-preserving change of chart.

## 7. Finite normalization checks

Run
~~~bash
python3 experiments/check_free_boundary_cardinal_factorial.py
~~~
The [script](../experiments/check_free_boundary_cardinal_factorial.py)
evaluates the original Newton products and cardinal sum directly.
It compares their physical values and first spectral normals with
the exact finite cyclotomic-factorial formula, at \(N=2,\ldots,9\)
and two complex indices. The odd simple root is checked only in
value. The saved [result](../repro/results/research-free-boundary-cardinal-factorial.json)
contains 48 physical-jet checks at 100 digits, with no failure.

It also records 24 off-grid comparisons through both parities,
at \(N=16,17,32,33,64,65\), including a complex boundary angle
and its derivative. Those records illustrate the projection error;
they are not used to prove its exponential decay. The proof is
the full Fourier-tail estimate (17)--(18) and the analytic
continuation argument (19)--(22).

The same 48 physical-jet checks and 24 off-grid diagnostics were
also run at 130 decimal digits. Their
[record](../repro/results/research-free-boundary-cardinal-factorial-root.json)
retains both script and factorial-dependency hashes.

## 8. The full edge kernel on a deep imaginary boundary

Positivity of the original edge geometry does not extend the full
quantum edge packet to its entire geometric domain. This can be
seen directly in the original Newton sum, without moving a cycle.
Write
\[
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u),
 \qquad D=N-1,\qquad M_\infty=4G/\pi.
 \tag{26}
\]
Fix a real number \(H>0\) and take \(t=-iH,u=0\). The original
positive-edge coordinates are
\[
 a=\tan(t/2)=-i\tanh(H/2),\qquad b=0,\qquad
 q=\sqrt{1+a^2+b^2}=\operatorname{sech}(H/2)>0.
 \tag{27}
\]
Thus the strict positive-domain inequality
\(\Re q>\sqrt{(\Re a)^2+(\Re b)^2}\) holds for every finite
\(H\). These are positive original tetrahedra, not a different
choice of shapes.

The geometrically selected edge phase is real on this path. Its
original period differential gives
\[
 \frac{d}{dH}\psi(-iH,0)
   =\frac1\pi\arcsin\!\bigl(\tanh(H/2)\bigr)<\frac12,
 \qquad
 \psi(-iH,0)<M_\infty+\frac H2.
 \tag{28}
\]
Here the branch is continued from \(H=0\); see the
[original positive-edge phase](research_positive_edge_volume_identity.md),
equation (3), and the
[zero-power edge calculation](research_zero_power_internal_boundary_theorem.md),
Section 1.

For even \(N\), however, every summand in (26) is positive.
Indeed all physical roots \(c_r=2\cos((2r+1)\pi/N)\) are
strictly greater than \(-2\), and the original products
\(e_j(z)=S_j^{-2}\prod_{r<j}(c_r-z)\) are positive at both
\(z=-2\) and \(z=-2\cosh H\). The last Newton polynomial has
the exact expression
\[
 e_D(z)=\frac{(-1)^D P_N(z)}{N^2(z-c_0)},\qquad
 P_N(z)=2T_N(z/2)+2.
 \tag{29}
\]
Using \(P_N(-2)=4\) and
\(P_N(-2\cosh H)=2\cosh(NH)+2\), we obtain
\[
 K_N(-iH,0)\ge
 e_D(-2\cosh H)e_D(-2)
 =\frac{4\{2\cosh(NH)+2\}}
 {N^4(2\cosh H+c_0)(2+c_0)}.
 \tag{30}
\]
Consequently
\[
 \liminf_{\substack{N\to\infty\\N\ \mathrm{even}}}
       \frac1N\log K_N(-iH,0)\ge H.
 \tag{31}
\]
For every fixed \(H>2M_\infty\), this rate exceeds the selected
geometric rate in (28). For example \(H=4\) suffices since
\(G<1\) and \(\pi>3\). At that point even a bound by a fixed
polynomial times \(e^{N\psi(-4i,0)}\) is impossible.

This is a statement about the full finite kernel. It does not
contradict a retained low-index edge asymptotic, or any theorem
which first controls the omitted wires in the complete original
source. At odd levels \(-2\) is a simple physical root and the
corresponding high-index terms vanish; the positive even-level
term in (30) must therefore be retained when extending a contour
argument along the full level sequence. A positive geometric
domain by itself is not a domain of validity for the same full
quantum edge packet.
