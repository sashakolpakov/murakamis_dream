# Calibrated overlap criteria for the original three/four observation

Research deduction, 7 November 2026. This note specializes an
almost-invariant-vector argument to the prescribed ordinary
\((3,4)\) source. It gives exact sufficient inequalities, including
the full original forcing and normal data. The sufficient overlap
conditions are not asserted to hold. It also proves that the
original real-period summands do not share one nonnegative phase.
No numerical evaluation is used.

The target overlap may itself be exponentially small. The
[proved same-sign/reflected comparison](research_complete_boundary_coefficient_transport.md),
Section 7, shows that this happens for actual solved sources, so
subexponential loss cannot be imposed as a general principle.

## 1. The actual observation and its positive norm

Use the original Newton coefficient norm and conventions
\[
 D=N-1,\qquad \eta=(-1)^D,\qquad
 A_n=JM^n=A_n^T,\qquad v=v(-2),\qquad w_n=A_nv .
 \tag{1}
\]
All \(N\) coordinates belong to the full Hermite algebra.
The [coefficient-transport theorem](research_complete_boundary_coefficient_transport.md),
equations (5), (24)--(26), gives
\[
\begin{split}
 Z_N&:=v^TA_3A_4v=w_3^Tw_4
                  =\langle\overline{w_3},w_4\rangle,\\
 \overline{w_n}&=w_{-n},\qquad
 \|w_n\|^2=\mathcal P_{-n,n,N}(-2,-2)>0.
\end{split}
 \tag{2}
\]
The inner product is conjugate-linear in its first entry.
There is no additional scalar in (2).

For the actual half-band interpolants \(W_{n,N}\), the same
coefficient is
\[
 Z_N=N\int_0^1 W_{3,N}(t)W_{4,N}(t)\,dt,\qquad
 \|w_n\|^2=N\int_0^1|W_{n,N}(t)|^2\,dt .
 \tag{3}
\]
Both parities satisfy this exact full-period identity. Moving
the complete integration period does not insert conjugation.
Equivalently, in the unitary half-band Fourier coordinates,
\[
 Z_N=\sum_{\ell\in\Lambda_N}
        \widehat w_3(\ell)\widehat w_4(-\ell),\qquad
 \|w_n\|^2=\sum_{\ell\in\Lambda_N}|\widehat w_n(\ell)|^2.
 \tag{4}
\]
Thus Plancherel estimates the two norms, and Cauchy--Schwarz
gives the upper bound \(|Z_N|\le\|w_3\|\|w_4\|\).
It gives no lower bound for (4).

There is also an exact crossing relation specific to this pair:
\[
 w_4=M^Tw_3.
 \tag{5}
\]
Indeed \(M^T=JMJ\), so \(M^TJM^3v=JM^4v\).
Let \(\mathfrak C\) be coefficientwise conjugation and set
\(\mathfrak A=\mathfrak C M^T\). Since \(\overline M=M^{-1}\),
\[
 \mathfrak A^2=I,\qquad
 \mathfrak A w_n=w_{-n-1},\qquad
 Z_N=\langle\mathfrak A w_3,w_3\rangle .
 \tag{6}
\]
This is an anti-linear involution, not a proved almost-invariance
statement for \(w_3\). It is not antiunitary in the original
coefficient norm: that would make \(M^T\) unitary, contradicting
its original nontrivial Jordan blocks. This does not exclude
making the involution alone antiunitary in another metric.
Such a metric change must retain the original observation.

There is a source-specific obstruction to exact positivity
on the undeformed real period.

**Proposition 1.** For every \(N\ge15\), the original summands
\(w_{3,j}w_{4,j}\) cannot all have one nonnegative phase.
Neither can the real-period function \(W_{3,N}(t)W_{4,N}(t)\).

*Proof.* Put \(\theta=\pi/N,\ q=e^{i\theta}\), and
\[
 E=e_1(-2)=\frac1{4\sin^2(\theta/2)}>0,\qquad
 a=\frac1{2\cos\theta}>0,\qquad L=E+a.
 \tag{6a}
\]
The original crossing has the upper-left block
\(\kappa_N\left(\begin{smallmatrix}1&0\\-q&-q^2\end{smallmatrix}\right)\).
Its powers give exactly
\[
 w_{n,D}=\kappa_N^n,\qquad
 \frac{w_{n,D-1}}{\kappa_N^n}
   =(-q^2)^nE-q\sum_{k=0}^{n-1}(-q^2)^k
   =(-q^2)^nL-a \qquad(n\ge1).
 \tag{6b}
\]
The identity \(q/(1+q^2)=a\) proves the last equality.
Consequently the last product is \(\kappa_N^7\), whereas
\[
 \frac{w_{3,D-1}w_{4,D-1}}{\kappa_N^7}
       =-q^{14}L^2+aL(q^6-q^8)+a^2 .
 \tag{6c}
\]
Its imaginary part is
\[
       -L^2\sin(14\theta)-2aL\cos(7\theta)\sin\theta<0,
 \tag{6d}
\]
because \(0<14\theta<\pi\) and \(0<7\theta<\pi/2\).
The two nonzero products therefore do not have the same phase.
The exact sampled values \(W_{n,N}(j/N)=w_{n,j}\)
give the real-period assertion. \(\square\)

This does not exclude approximate phase alignment on the indices
that dominate a norm, or a useful complex contour. It rules out
the stronger exact real-period positivity shortcut for the
prescribed source.

## 2. The correctly calibrated overlap scale

Let \(\mathcal W_{34}\) be the original stationary action at
the complete ordinary boundaries, and put \(M_{34}=\Re\mathcal W_{34}\).
The [actual pair source](research_mixed_three_four_ordinary_pair_target.md),
equations (8)--(10), fixes a nonzero plateau coefficient \(a_{34}\)
and the comparison term
\[
 T_N=\kappa_N^3N^{-3/2}a_{34}e^{N\mathcal W_{34}}.
 \tag{7}
\]
This normalization is fixed by the original source, not by
the two positive norms. Its geometric calibration is already
proved by the mixed boundary-germ theorem.

Define
\[
 u_N=\frac{\overline{w_3}}{\|w_3\|},\qquad
 v_N=\frac{w_4}{\|w_4\|},\qquad
 \chi_N=\langle u_N,v_N\rangle,\qquad
 \tau_N=\frac{T_N}{\|w_3\|\|w_4\|}.
 \tag{8}
\]
Then \(Z_N=\|w_3\|\|w_4\|\chi_N\) exactly. In particular,
for any fixed \(c>0\),
\[
 |\chi_N|\ge c|\tau_N|
 \quad\Longrightarrow\quad
 |Z_N|\ge c|a_{34}|N^{-3/2}e^{NM_{34}}.
 \tag{9}
\]
The stronger relative estimate
\(|\chi_N-\tau_N|\le\varepsilon_N|\tau_N|\) gives
\(|Z_N-T_N|\le\varepsilon_N|T_N|\).

Writing \(\lambda_{n,N}=N^{-1}\log\|w_n\|\), the exact required
scale is
\[
 \frac1N\log|\tau_N|
 =M_{34}-\lambda_{3,N}-\lambda_{4,N}
       -\frac{3\log N}{2N}+\frac{\log|a_{34}|}{N}.
 \tag{10}
\]
Neither a norm rate nor the sign or size of its excess over
\(M_{34}\) is asserted here. In particular (9) allows the
overlap to have a strictly negative exponential rate.
The actual long-power result cited above has just such a loss,
\(\Delta_n=16\pi^3/n^6+O(n^{-7})>0\), for sufficiently large
fixed \(n\); it does not determine the \((3,4)\) overlap.

Here is a sufficient coercivity test with that scale retained.
Suppose specified unitary operators \(U_{j,N}\), unit scalars
\(\zeta_{j,N}\), a unit vector \(z_N\), and \(\gamma_N>0\)
have been proved to satisfy
\[
 \sum_j(U_{j,N}-\zeta_{j,N})^*
            (U_{j,N}-\zeta_{j,N})
       \ \ge\ \gamma_N(I-z_Nz_N^*).
 \tag{11}
\]
Set
\[
 \epsilon_N^2=\gamma_N^{-1}
       \sum_j\|(U_{j,N}-\zeta_{j,N})v_N\|^2<1,\qquad
 \beta_N=|\langle u_N,z_N\rangle|.
\]
Orthogonal projection onto \(z_N\) and the triangle inequality give
\[
 |\chi_N|\ge
 \beta_N\sqrt{1-\epsilon_N^2}
           -\sqrt{1-\beta_N^2}\,\epsilon_N.
 \tag{12}
\]
Indeed the component of \(v_N\) perpendicular to \(z_N\)
has norm at most \(\epsilon_N\), while the corresponding
component of \(u_N\) has norm \(\sqrt{1-\beta_N^2}\).
Thus a sufficient actual lower-bound criterion is that the
right side of (12) be at least \(c|\tau_N|\).
The gap, the defect, the overlap with the prescribed \(u_N\),
and their calibration to (10) are separate requirements.
In particular, a merely small defect need not be small enough
when \(\beta_N\) or \(\tau_N\) is exponentially small.

No operators or inequalities satisfying (11)--(12) for this
source have been constructed here. The preserved original
form \(M^*JM=J\) is indefinite and does not supply (11).
The real full-jet change of coordinates described in the
[Fourier lower-bound audit](research_fourier_lower_bounds_and_almost_invariance.md),
Section 18, gives a positive pullback metric but preserves
the bilinear overlap in (2); it does not replace it by a norm.

## 3. A dual test using the actual forced coefficient equation

There is a source-specific alternative that requires no
positive unitarization or invented invariant line. Write
\[
 \mathcal D_4=A_4 Z^T A_4^{-1},\qquad B_4=\mathcal D_4+2I ,
 \tag{13}
\]
where \(Z\) is the original Newton multiplication-by-color matrix.
The exact coefficient equation, with its original last coordinate, is
\[
 B_4w_4=\frac{2(1-\eta)\kappa_N^4}{N^2}\mathbf e_0,
                 \qquad \mathbf e_D^Tw_4=\kappa_N^4.
 \tag{14}
\]
For any trial pair \(b_N\in\mathbb C^N,t_N\in\mathbb C\), set
\[
\begin{split}
 r_N&=B_4^*b_N+t_N\mathbf e_D-\overline{w_3},\\
 q_N&=\kappa_N^4\left(
       \overline{t_N}+\frac{2(1-\eta)}{N^2}
                                  \overline{(b_N)_0}\right).
\end{split}
 \tag{15}
\]
Taking the inner product with the actual \(w_4\) gives
the exact identity
\[
                   Z_N=q_N-\langle r_N,w_4\rangle .
 \tag{16}
\]
Consequently a proved upper bound \(L_N\ge\|w_4\|\), together with
\[
 |q_N-T_N|+\|r_N\|L_N\le\varepsilon_N|T_N|,
 \tag{17}
\]
implies \(|Z_N-T_N|\le\varepsilon_N|T_N|\). For a lower bound
alone, it suffices that
\[
        |q_N|-\|r_N\|L_N\ge c|T_N|.
 \tag{18}
\]
At odd levels the forcing term vanishes, but the normalization
term \(\kappa_N^4\overline{t_N}\) remains. At even levels the
forcing is \(4\kappa_N^4/N^2\); it cannot be dropped.

The augmented map \(f\mapsto(B_4f,\mathbf e_D^Tf)\) is
injective by the original uniqueness theorem. Hence exact
adjoint solutions to \(r_N=0\) exist in finite dimension.
This existence gives neither a useful bound on their size
nor the observation \(q_N\) at the scale (7). A homogeneous
adjoint quasimode with small \(B_4^*b_N\) is not an
approximation to the prescribed right side
\(\overline{w_3}-t_N\mathbf e_D\) in (15).
The [original adjoint-overlap example](research_original_almost_invariance_and_observation.md),
Section 3, explicitly shows how the endpoint overlap can
lose the whole gain from a small residual.

## 4. What the existing symmetry and source estimates provide

The verified symmetries used above give sign reversal
\(w_n\mapsto w_{-n}\), the indefinite conserved form,
and the exact adjacent transfer (5). They do not give an
alignment of \(w_4\) with \(\overline{w_3}=w_{-3}\),
or a dual pair satisfying (17). Fourier transformation
and a faithful change to physical jets preserve this
distinction, including every repeated-root normal.

The existing positive three-cycle similarity does not change
that conclusion. With \(H=M^*M>0\), equation (6) of
[the positive-cycle theorem](research_positive_three_crossing_cycle.md)
specializes to
\[
 M A_3A_4M^{-1}=\kappa_N^2 H^2M .
\]
Thus the actual complete vector gives
\[
 Z_N=\kappa_N^2
       \left\langle H M^{-*}v,\ H M^2v\right\rangle ,
 \tag{18a}
\]
where \(M^{-*}=(M^*)^{-1}\).
Indeed the first vector before applying \(H\) has adjoint
\(v^TM^{-1}\), since \(v\) is real. The two vectors in
(18a) are different prescribed adapters. The positivity of
\(H\) supplies a positive spectral measure for a matching
vector, but (18a) has mixed spectral weights. No alignment
or noncancellation estimate for these adapters is implied.

The exact same scalar also has the complete one-circle source
\[
 Z_N=\kappa_N^3N^2\oint
 U_{0,N}(-2,X)V_{1,N}(-2,X)\frac{dX}{2\pi iX}.
 \tag{19}
\]
Its known plateau Gaussian is (7), while the complete
complementary cycle remains to be bounded. Thus (17)
is an alternative target to that particular source estimate,
not a result already supplied by the local kernel theorem.
Either method must control the prescribed scalar at the
same original action.

These criteria concern the complete-point observation.
A whole ordinary boundary packet additionally requires
uniform complex-color control and fixed derivatives.
The long-filling insertion theorem also requires its
calibrated outside-color gap. Neither follows from a
complete-point lower bound alone, and no new knot-family
conclusion is asserted.
