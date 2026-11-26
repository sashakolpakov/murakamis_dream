# Reflection controls the full conditional phase at negative height

Research proof, 4 November 2026. This is an analytic phase comparison,
including the full high half-period and the right endpoint join. It does
not replace the exact finite conditional sum by a periodic interpolant,
discard a wrapped Fourier term, or establish a full-source asymptotic.
Completed source certificates and frozen manuscripts are unchanged.

## 1. A circular second-difference inequality

Use the original normalized primitive
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
 \tag{1}
\]
For \(y<0\), put \(R=e^{2\pi y}\in(0,1)\) and
\(J_R(x)=\Re g(x+iy)\). The absolutely convergent disk series gives
\[
 J_R(x)=-\frac1{2\pi}\sum_{k\ge1}
               \frac{R^k\sin(2\pi kx)}{k^2}.
 \tag{2}
\]
Thus \(J_R\) is odd and one-periodic, and \(J_R(0)=J_R(1/2)=0\).
Its derivatives satisfy
\[
 J_R'(x)=\log|1-Re^{-2\pi ix}|,\qquad
 J_R''(x)=\frac{2\pi R\sin(2\pi x)}
                         {1+R^2-2R\cos(2\pi x)}>0
                     \quad(0<x<1/2).
 \tag{3}
\]
In particular \(J_R(x)<0\) throughout that open half-period.

**Lemma 1.** For \(0<x,c<1/2\), define
\[
 D_{c,R}(x)=J_R(x+c)+J_R(x-c)-2J_R(x).
\]
Then
\[
 D_{c,R}(x)\ge
 \frac{R\sin(2\pi x)[1-\cos(2\pi c)]}{\pi(1+R)^2}>0.
 \tag{4}
\]

Indeed, with
\(A=|1-Re^{-2\pi i(x+c)}|^2\) and
\(B=|1-Re^{-2\pi i(x-c)}|^2\),
\[
 A-B=4R\sin(2\pi x)\sin(2\pi c)>0,
 \qquad
 \partial_cD_{c,R}(x)=\tfrac12\log(A/B).
 \tag{5}
\]
For \(A\ge B>0\), \(\log(A/B)\ge(A-B)/A\), while
\(A\le(1+R)^2\). Integrating the resulting lower bound from
\(c=0\), where \(D_{0,R}=0\), proves (4).
The series (2) converges uniformly also as \(R\uparrow1\).
Consequently (4) extends to \(R=1\) by continuity, even when a
derivative in (5) has a logarithmic singularity. The endpoint values
and strict negativity of \(J_1\) on \((0,1/2)\) follow as well,
or directly from \(J_1''=\pi\cot\pi x>0\).

## 2. Every high-half point is below its low-half mirror

Fix real \(0<a,b<1/2\), and retain the original phases
\[
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,
 \quad H_{\epsilon,R}(x)=\Re Q_\epsilon(x+iy;a,b),
 \quad\epsilon=0,1.
 \tag{6}
\]
For \(y=0\), every phase value here means the continuous limit
from the lower half-plane. At negative height all three dilogarithm
arguments lie in the open unit disk, even as \(x+a\) or \(x+b\)
crosses one. No branch wall is crossed in (6).

Oddness and periodicity of \(J_R\), together with the fact that
the real part of the original chirp is independent of \(x\), give
the exact identity
\[
 H_{\epsilon,R}(x)-H_{\epsilon,R}(1-x)
   =D_{a,R}(x)+D_{b,R}(x)-2\epsilon J_R(x)>0
                    \quad(0<x<1/2).
 \tag{7}
\]
This holds for every \(0<R\le1\), without a selected-root relation
or an assertion that the high half has only one critical point.
It remains valid if the derivative on that half has several zeros.

**Theorem 2.** Let \(s_*=x_*+ih_*\) be either original conditional
root supplied by the
[global cotangent theorem](research_mixed_global_cotangent_roots.md),
for real \(a,b\in(0,1/2)\), and assume \(h_*\le0\).
Then \(x_*\) is the unique global maximizer of
\(\Re Q_\epsilon(x+ih_*;a,b)\) on the entire period \([0,1]\).
The maximum is nondegenerate. The whole high half \([1/2,1]\)
has a strict gap below that maximum.

The [real conditional contour theorem](research_mixed_real_conditional_contour_geometry.md)
already gives the unique nondegenerate maximum on \([0,1/2]\),
including strict inequalities at its endpoints. Equation (7) controls
every point in \((1/2,1)\) by its reflected point in \((0,1/2)\).
At \(x=1\), periodicity gives the rate at zero; at \(x=1/2\)
the existing endpoint inequality applies. This proves the theorem.
If the real parameters range over a compact set on which \(h_*\le0\),
continuity and compactness make the entire high-half gap uniform.
Uniform convergence of (2) includes parameter limits with \(h_*=0\).

The same comparison controls the right vertical endpoint. Below the
real axis the exact primitive is periodic, and
\[
 Q_\epsilon(s+1;a,b)=Q_\epsilon(s;a,b)+2\pi ia.
 \tag{8}
\]
The two vertical lines \(\Re s=0,1\) therefore have identical real
rates. The left-join inequality in the cited real-contour theorem yields
\[
 \max_{h_*\le v\le0}\Re Q_\epsilon(1+iv;a,b)
  =\Re Q_\epsilon(ih_*;a,b)
  <\Re Q_\epsilon(s_*;a,b).
 \tag{9}
\]
The equality uses its monotonicity along the left endpoint; at height
zero it is understood as the lower-boundary limit. This gap is uniform
on the same compact parameter sets.

## 3. The true extra Fourier forcing rate

There is a useful stronger comparison when an extra inverse-factorial
rate is replaced by its true Fourier upper envelope. At any fixed
\(y\le0\), define the continuous rate profile
\[
 E_R(x)=H_{0,R}(x)+\max\{-J_R(x),0\}.
 \tag{10}
\]
It is \(H_{1,R}\) on the low half and \(H_{0,R}\) on the high half.
For \(0<x<1/2\),
\[
 H_{1,R}(x)-H_{0,R}(1-x)
       =D_{a,R}(x)+D_{b,R}(x)-J_R(x)>0.
 \tag{11}
\]
Thus at the selected type-four height \(h_*\le0\), (10) has the
same unique global maximum and a uniform high-half gap as in Theorem 2.
At the vertical endpoints \(J_R(0)=J_R(1)=0\), so their rates also
agree with (9).

The maximum in (10) is precisely the factorial-versus-forcing rate
appearing in the general Fourier-polynomial upper estimate at a negative
height. This corollary compares the explicit rate profile; it does not
identify an unspecified finite coefficient contour with that profile.
In particular it supplies no estimate for an additional wrapped term.

## 4. Exact reflection of the original finite interpolation

Let \(G_N\) be the fixed sine-factorial interpolation in
[the exact factorial theorem](exact_factorial_interpolation_and_complex_contours.md),
and set
\[
 P_N(w)=e^{-i\pi w(w+1)/(2N)+i\pi w/2}G_N(w).
 \tag{12}
\]
The positive-base Gamma product defining \(G_N\) is Schwarz real;
its meromorphic continuation has the same property. Its exact recurrence
therefore gives
\(P_N(w+1)=(1-e^{-2\pi i(w+1)/N})P_N(w)\) and
\(P_N(j)=(r;r)_j\) for \(0\le j<N\). For real \(a,b\), the function
\[
 T_N(s)=e^{2\pi iNa s}
       \frac{P_N(N(s+a))P_N(N(s+b))}{P_N(Ns)^{2+\epsilon}}
 \tag{13}
\]
matches every original row of \(\mathcal L_{\epsilon,N}(a,b)\) at
\(s=j/N\), including any physical zero rows. This follows directly
from the recurrence, for arbitrary real outer parameters; equality only
on a physical outer grid is not being used.

Schwarz reflection, including the explicit prefactor in (12), proves
the exact modulus identities
\[
 \begin{split}
 \frac{|P_N(N(x+iy))|}{|P_N(N(x-iy))|}
     &=e^{\pi Ny(2x-1)+\pi y},\\
 \frac{|T_N(x-iy)|}{|T_N(x+iy)|}
     &=e^{2\pi Ny\{a-b+\epsilon(x-1/2)\}+\epsilon\pi y}.
 \end{split}
 \tag{14}
\]
They hold wherever the quotients are defined and extend as modulus
equalities by limits. In particular they apply to every \(x\in[0,1]\)
at a fixed nonzero height. To verify the first exponent, the real part
of the exponent in (12) at \(w=N(x+iy)\) is
\(\pi Ny(x-1/2)+\pi y/2\). For the second, the original chirp
contributes \(4\pi Nay\) to the log modulus ratio. The two numerator
and \(2+\epsilon\) denominator factors then give exactly (14).
No leading-phase identity, factorial-wall continuation, or unmentioned
cyclotomic factor substitutes for this finite identity.

On a compact real outer set put
\(\Lambda_K=\max_K|a-b|+\epsilon/2<1\). The upper horizontal
cotangent remainder at height \(Y>0\), with its literal penalty
\(e^{-2\pi NY}\), satisfies the exact comparison
\[
 |T_N(x+iY)|e^{-2\pi NY}
 \le |T_N(x-iY)|
       e^{-2\pi NY(1-\Lambda_K)-\epsilon\pi Y},
 \qquad 0\le x\le1.
 \tag{15}
\]
Thus an established bound on the complete lower horizontal interpolation
also bounds the upper alias, with a strict exponential reserve. The
usual polynomial cotangent prefactors do not change this reserve.
This statement compares the exact row functions; it does not yet supply
their lower-half asymptotic across the shifted factorial walls.

## 5. Remaining finite-source obligations and reproduction

Theorem 2 controls the whole periodic analytic phase and both endpoint
vertical rates, retaining its original chirp and absolute normalization.
A complete source proof must still establish the required lower-half
asymptotic and uniform endpoint bounds for (13) across every shifted
factorial wall, exhaust its actual contour currents, and retain any
additional wrapped factors in a proposed coefficient representation.
Periodicity of (6) does not imply periodicity of the off-grid finite
summand (13), and a boundary phase gap is not a uniform finite-factorial
bound at a moving endpoint cut.
No finite-sum lower bound or mixed-word volume theorem is asserted here.

Run

    python3 experiments/check_mixed_negative_height_full_period.py --precision 320

The checker verifies the derivative, finite reflection and chirp identities
exactly, together with the elementary logarithmic inequality reduction
and the current bindings of the two analytic inputs. The global signs,
uniform limits and compactness arguments above are analytic proofs;
there is no sampled contour maximum or root count in the computation.
