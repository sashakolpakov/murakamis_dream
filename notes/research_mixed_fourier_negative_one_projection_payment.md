# A reflected Fourier weight pays the one-negative-crossing endpoint

Research deduction, 7 November 2026. The actual endpoint observation
after one negative crossing is exactly a reflected reciprocal-factorial
Fourier polynomial. Its two absolute-rate alternatives are controlled
by the already paid coherent half row and true endpoint of the original
cap. This proves a finite projection gap on the whole original incoming
plateau, including both signs of the incoming type-three height.

The proof retains the \(M^*J\) observation until its exact finite
orthogonality simplifies it. It does not continue a relative Fourier
packet to an unproved reflected domain, and it does not identify an
action for the complete crossed source. No numerical evaluation is used.

## 1. Exact cancellation of this signed observation

Use \(N\ge2\), \(D=N-1\), and the original conventions
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad r=Q^{-1},\quad
 P_j=(r;r)_j,\quad F_j=(Q;Q)_j,\quad
 \kappa=q^{D^2/2},\quad X=e^{-2\pi ia},\quad Y=e^{2\pi iy}.
 \tag{1}
\]
Let \(d_N\) be the degree-less-than-\(N\) polynomial satisfying
\(d_N(r^b)=P_b^{-1}\), and define the Laurent polynomial
\[
                 d_N^\star(X)=\overline{d_N(1/\overline X)}.
 \tag{2}
\]
Its band is \([-D,0]\). Let \(Z_N\), \(\mathcal M_n\), and
\(\Pi_0\) be the original cap, signed crossing and first Fourier
projector in
[the signed coefficient dictionary](research_mixed_fourier_signed_crossing_coefficients.md).

**Proposition 1.** At every level and both parities,
\[
 \boxed{\quad
 [f_0]\mathcal M_{-1}Z_N=\kappa^{-1}d_N^\star(X),\qquad
 \Pi_0\mathcal M_{-1}Z_N(a,y)
                  =\kappa^{-1}d_N^\star(X)f_0(y).
 \quad}
 \tag{3}
\]
Here
\[
                 f_0(y)=\frac{e^{-\pi iDy}(1-Y^N)}{N(1-Y)}
 \tag{4}
\]
is unchanged.

*Proof.* The full physical-node dictionary, with its original
Gram observation, gives
\[
 [f_0]\mathcal M_{-1}Z_N\big|_{X=r^b}
          =\frac{(-q)^{-b}}{\kappa N}(M^*M\mathbf e_0)_b.
 \tag{5}
\]
The original crossing entries from
[terminal powers](research_terminal_powers_qbinomial.md),
equation (2), are
\[
 M_{jb}=\kappa(-1)^jq^{j(b+1)}
                   \frac{S_j}{S_bS_{j-b}},\qquad
 M_{j0}=\kappa(-1)^jq^j,\qquad
 S_j=i^jq^{-j(j+1)/2}F_j .
 \tag{6}
\]
The \(S_j\) are real and positive for \(0\le j<N\). Thus
\[
 (M^*M\mathbf e_0)_b
    =q^{b^2}\sum_{j=b}^{N-1}Q^{-bj}{j\brack b}_Q.
 \tag{7}
\]
For \(b<N\), the expression
\[
 {j\brack b}_Q
       =\frac1{F_b}\prod_{m=0}^{b-1}(1-Q^{j-m})
 \tag{8}
\]
is a degree-\(b\) polynomial in \(Q^j\), with leading
coefficient
\((-1)^bQ^{-b(b-1)/2}/F_b\).
It vanishes at \(j=0,\ldots,b-1\), so these indices can
be inserted in (7). After multiplication by \(Q^{-bj}\),
the only exponent divisible by \(N\) is zero. Full-period
root orthogonality consequently gives
\[
 (M^*M\mathbf e_0)_b
   =Nq^{b^2}\frac{(-1)^bQ^{-b(b-1)/2}}{F_b}
   =\frac{N(-1)^bq^b}{F_b}.
 \tag{9}
\]
This includes \(b=0\), where the empty product is one.
Equations (5), (9) yield the physical values
\(\kappa^{-1}/F_b\).
At the same nodes, (2) has value
\(\overline{P_b^{-1}}=F_b^{-1}\).
Both expressions have band \([-D,0]\), so uniqueness on
all \(N\) nodes proves (3). No quotient normal or upper
triangular endpoint is discarded in this calculation.
\(\square\)

The separate identity
\(C_{0,N}(X,1)=N d_N^\star(X)\), already proved in
[boundary strip bounds](research_mixed_boundary_strip_bounds.md),
equation (15), is consistent with (3).
It is the type-three conditional kernel \(C_0\).
The original projection of \(Z_N\) itself contains \(C_1(X,1)\);
these are not interchangeable sources.

## 2. The correct reflected parameter and both rate alternatives

In the incoming parameter,
\[
 d_N^\star(e^{-2\pi ia})
            =\overline{d_N(e^{-2\pi i\overline a})}.
 \tag{10}
\]
The reflection changes \(h=\Im a\) to \(-h\), while keeping
\(x=\Re a\). In particular a negative incoming height becomes
a positive-height input of the Fourier polynomial.

The absolute bound in Section 5 of
[Fourier-weight continuation](research_mixed_fourier_weight_continuation.md)
holds on every compact subset of \(0<\Re z<1\).
More explicitly, its full four-sided residue identity
retains the forcing factor. If \(z=\overline a\) ranges in
that compact reflected strip, choose one fixed contour
height \(H>\sup|\Im z|\). Its proof gives
\[
 \left|d_N(e^{-2\pi iz})-\widehat P_N(Nz)^{-1}\right|
 \le C_HN^{-1/2}|1-e^{-2\pi iNz}|\,e^{Nb(H)},\qquad
                  b(H)=-\log(1-e^{-2\pi H})\longrightarrow0.
 \tag{11a}
\]
This is the estimate before its forcing was bounded to
obtain equation (17) of that source. At the reflected
parameter it retains \(|1-(1/\overline X)^N|\), bounded by
\(2e^{2\pi N(-h)_+}\), rather than set to zero.
The regular-strip factorial packet supplies the other
rate \(-\Re g(\overline a)\). Choose \(H\) once with
\(b(H)<\tau\), and combine the two terms. This gives
\[
 |d_N^\star(e^{-2\pi ia})|
 \le C_\tau N^{-1/2}
   \exp N\left\{\max\{-\Re g(\overline a),\,2\pi(-h)_+\}
                                                   +\tau\right\}.
 \tag{11}
\]
Both terms are necessary in this use of the theorem. Its
relative packet on the lower half-plane is not asserted
at the reflected positive-height inputs.

On a compact output neighborhood with \(|Y|<1\), equations
(3)--(4), (11) therefore give the unallocated upper rate
\[
 \mathcal E_{-1}(a,y)
     =\max\{-\Re g(\overline a),\,2\pi(-h)_+\}+\pi\Im y,
 \tag{12}
\]
with prefactor \(C_\tau N^{-3/2}\) and tolerance \(\tau\).
No division by a Fourier weight or its zeros occurs.

## 3. The coherent half row pays the reflected-factorial alternative

Fix an actual correlated reference \(a_*\in K_{3+\eta}\),
\(\eta=0,1\), output \(y=x_0\), and incoming target
\[
 a=x+i\Im a_*,\qquad x\in P=[11/50,9/20].
 \tag{13}
\]
When \(\eta=1\), retain its original negative unselected height.
Use the original plane
\[
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                    -\frac{(x-\Re a_*)^2}{2500000}.
 \tag{14}
\]
Write
\[
 I_a(s)=\int_0^s\log|1-Xe^{-2\pi it}|\,dt,\qquad
 \mathcal J_{\rm W}=\Re I_{\rm W}(1/2,Y)>0.
 \tag{15}
\]
The positivity in (15) is the proved exterior degree-root
inequality \(|R(t,0,Y)|>1\), integrated on the half-degree
interval. The original coherent half-row rate is
\[
 \mathcal E_{\rm half,\eta}(a)
   =I_a(1/2)-\pi h+\pi\Im y+\mathcal J_{\rm W}
                                 -\frac{\eta}{2}\Re g(a)
             <B_\eta(x)-\frac1{35000}.
 \tag{16}
\]
These are equations (18)--(20) of
[uniform vertical-tail payment](research_mixed_fourier_vertical_tail_payment.md),
using the completed
[coherent high-tail theorem](research_mixed_fourier_right_cap_coherent_high_tail_payment.md).
In particular (16) is an individual coherent-row rate comparison.

All real arguments \(x\) through \(x+1/2\) stay in \((0,1)\).
The original primitive and its Schwarz relation give exactly
\[
\begin{split}
 I_a(1/2)&=\Re\{g(a+1/2)-g(a)\},\\
 \Re g(\overline a)&=\Re g(a)+\pi h(1-2x),\\
 \Re g(\overline a+1/2)&=\Re g(a+1/2)-2\pi hx.
\end{split}
 \tag{17}
\]
The first equality also holds at \(h=0\), by integrating the
original real logarithm. Thus
\[
\begin{split}
 \mathcal E_{\rm half,\eta}(a)
 &-\left\{-\Re g(\overline a)+\pi\Im y
                                  -\frac{\eta}{2}\Re g(a)\right\}\\
 &=\Re g(\overline a+1/2)+\mathcal J_{\rm W}>0.
\end{split}
 \tag{18}
\]

Here the strict sign is valid for either sign of \(h\).
Indeed \(\Re g(z)>0\) on \(1/2<\Re z<1\) at every finite
height. In the lower half-plane, the original disk formula
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}
 \tag{19}
\]
has positive real part: its disk argument has angle in
\((0,\pi)\), and the radial derivative of
\(\Im\operatorname{Li}_2(\rho e^{i\theta})\) is
\(-\arg(1-\rho e^{i\theta})/\rho>0\), starting from zero.
The real boundary follows by continuity and strict positivity
of that integral. Above the axis, Schwarz reflection adds
\(\pi(\Im z)(2\Re z-1)>0\) to the lower reflected value.
This proves the sign in (18) throughout (13), without a
new quantitative primitive evaluation.

The other alternative in (12), with its incoming allocation,
is exactly the true endpoint rate
\[
 2\pi(-h)_++\pi\Im y-\frac{\eta}{2}\Re g(a)
                       <B_\eta(x)-\frac{387}{70000},
 \tag{20}
\]
already proved in
[endpoint payment](research_mixed_fourier_right_cap_endpoint_payment.md),
equation (20). Combining (16), (18), (20) yields
\[
 \mathcal E_{-1}(a,x_0)-\frac{\eta}{2}\Re g(a)
                      <B_\eta(x)-\frac1{35000}.
 \tag{21}
\]
This compares both original Fourier-polynomial branches,
not only a desired factorial term.

## 4. Finite and holomorphic consequences

Use the original admissible finite upper bound for the
incoming halfweight on (13), with its rate
\(-\eta\Re g(a)/2\). For every \(\tau>0\), equations
(3), (11), (21), allocating the tolerances in (11a) and
the halfweight below this single aggregate \(\tau\), prove
\[
 |d_N(X)|^{\eta/2}|\Pi_0\mathcal M_{-1}Z_N(a,x_0)|
 \le C_\tau N^{A_\tau}
             e^{N\{B_\eta(x)-1/35000+\tau\}}.
 \tag{22}
\]
After one smaller tolerance and polynomial absorption,
uniformly on the original compact families and both parities,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}|\Pi_0\mathcal M_{-1}Z_N(a,x_0)|
                      \le e^{N\{B_\eta(x)-1/70000\}}.
 \quad}
 \tag{23}
\]

There is also a local whole-source comparison. Let
\((a_*,x_0)\) be an actual center, and let \(\Phi\) be the
phase of the established
[holomorphic cap packet](research_mixed_fourier_right_cap_holomorphic_packet.md).
At this center (21) cancels the same incoming allocation
on both sides, giving
\[
          \mathcal E_{-1}(a_*,x_0)
                    <\Re\Phi(a_*,x_0)-1/35000.
 \tag{24}
\]
The rate (12) is continuous and its absolute finite bound
(11) is uniform on compact reflected parameter sets.
Shrink the holomorphic packet neighborhood so that the
gap in (24) remains strictly greater than \(1/70000\).
The original whole cap is nonzero there for sufficiently
large \(N\). On every smaller neighborhood \(U'\) and for
each fixed multi-index \(\alpha\), the exact holomorphic
ratio consequently satisfies
\[
 \boxed{\qquad
 \sup_{U'}\left|
 \partial^\alpha\left(\frac{\Pi_0\mathcal M_{-1}Z_N}{Z_N}\right)
                         \right|
                  \le C_{\alpha,U'}e^{-N/70000}.
 \qquad}
 \tag{25}
\]
For this deduction first choose a larger intermediate
neighborhood with strict room in the exponent and in (11),
then use the nonzero \(N^{-3/2}\) whole-cap packet there.
Cauchy's estimates give (25). No relative approximation
to the reflected Fourier polynomial is needed.

The denominator in (25) is the original \(Z_N\), not
\(\mathcal M_{-1}Z_N\). Equations (23), (25), together with
the separate
[two-negative-crossing payment](research_mixed_fourier_negative_two_projection_payment.md),
settle two actual short-run endpoint corrections at the
original action. They do not prove a nonzero packet or an
action-preservation theorem for either complete crossed
source. Such transport and the original ordinary closing
lower bound remain necessary before an iteration or an
arbitrary short-filling conclusion.
