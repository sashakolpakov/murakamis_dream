# Inverting an endpoint current retains a source correction

Private written research note, 15 November 2026.

The endpoint-current matching polynomial is a unit in the full finite
boundary algebra. Its inverse gives an exact identity after the
prescribed closing, with an inserted inverse coupon. It does not turn
the original Ward relation into scalar transport: the actual
spectator shift has an explicit commutator with that coupon.

There is also a concrete analytic distinction. The logarithmic-factorial
representative of an actual odd endpoint current has a simple zero
inside the lower physical window, at distance of order \(N^{-2}\) from
its real boundary. Its reciprocal has a pole whose contribution survives
the original trace normalization. The polynomial Hermite inverse cancels
this pole by an exactly specified correction. These facts concern the
original current and closing, with arbitrary polynomial exterior
spectators retained. They neither obstruct a coherent contour proof
that keeps the correction nor establish its geometric coefficient.

## 1. What the finite inverse does after closing

Put
\[
 N\ge3,\quad D=N-1,\quad \eta=(-1)^D,\quad \sigma=(-1)^N,
 \quad \theta=\pi/N,\quad s_1=2\sin\theta,\quad \rho=i s_1,
\]
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 \phi_N(f)=\eta N^2\sum_{P_N(c)=0}
               \operatorname{Res}_{z=c}\frac{f(z)\,dz}{P_N(z)}.
 \tag{1}
\]
All repeated roots and their first normals are included.
The original crossing is \(R=\kappa r_N\), with
\(\kappa=\exp(\pi iD^2/(2N))\).

For a current subset \(S\) in a finite circle tree, let
\(\mathcal E_{S,N}\) be its exact boundary matching polynomial. Assume
no even current power is zero. The boundary-unit theorem gives an
inverse \(J_{S,N}\) in the tensor product of the remaining physical
boundary algebras, including every mixed first normal:
\[
                  \mathcal E_{S,N}J_{S,N}=1.
 \tag{2}
\]
Consequently, for the actual exterior polynomial \(F_N\) and its
remaining original contraction \(\Lambda_N\),
\[
 \Lambda_N(F_N)=
 \Lambda_N(\mathcal E_{S,N}J_{S,N}F_N).
 \tag{3}
\]
By the grouped-current identity, the right side is precisely the source
with the specified Ward insertions at \(S\), and with the coupon
\(J_{S,N}\) inserted at its boundary before the exterior is closed.
This holds with shared outside variables and all exterior first
normals. It recovers the deleted-current exterior in (3); it does not
identify that exterior with the original filled component.
Common physical factors \(\prod_{v\in S}\kappa^{n_v}\) multiply the
inserted-current identity and must be retained if unnormalized
crossings are used.

The inverse has polynomial full-Hermite norm, by the boundary-unit
theorem. That bounds its physical jets, rather than every analytic
representative throughout a deformed contour.

## 2. The actual Ward operator and the inverse coupon

For the logarithmic coordinate \(z(x)=e^x+e^{-x}\), let
\(\hbar=2\pi i/N\). The actual adjoint spectator shift is
\[
 (\mathcal L A)(z(x))=
 \sum_{\epsilon=\pm1}
 \frac{\sinh(x+\epsilon\hbar)}{\sinh x}
                  A(z(x+\epsilon\hbar)).
 \tag{4}
\]
For polynomial \(A\) this is a polynomial; its apparent singularities
are removable. It descends to \(\mathcal A_N\). For
\(f_n=r_N^n\), define
\[
 \lambda_n=(-q)^n,\quad q=e^{\pi i/N},\qquad
 \mathcal D_n=\mathcal L-2\lambda_n M_{T_n(z/2)},
 \qquad \mathcal I_n(A)=\phi_N(f_nA).
 \tag{5}
\]
Here \(M_fA=fA\) and \(T_{-n}=T_n\).
The exact translated-contour Ward identity is
\[
                 \mathcal I_n(\mathcal D_n A)=\phi_N(W_{n,N}A).
 \tag{6}
\]
Its right side is the four-end-circle current of the original
logarithmic residue cycle.

For any polynomial coupon \(J\), multiplication commutes with the
second term of \(\mathcal D_n\), so
\[
 \mathcal D_n(JA)=J\mathcal D_nA+[\mathcal L,M_J]A,
 \tag{7}
\]
\[
 [\mathcal L,M_J]A(z(x))=
 \sum_{\epsilon=\pm1}
 \frac{\sinh(x+\epsilon\hbar)}{\sinh x}
 \bigl[J(z(x+\epsilon\hbar))-J(z(x))\bigr]
                    A(z(x+\epsilon\hbar)).
 \tag{8}
\]
Both sides are polynomials and the identities hold in the full
quotient, with removable points interpreted by continuation.
Thus applying (6) to an inverse-coupon spectator is exact, but its
transport retains (8). An inverse bound for multiplication alone
does not estimate or delete this term. The same formula applies
in each boundary variable of a tensor source, retaining all other
variables as coefficients.

## 3. An actual odd current has a zero inside the physical window

Take a single odd-current vertex with one outside incidence. The
exact grouped-current polynomial is
\[
 \mathcal E_{n,N}(z)=2U_N(z)+\eta n\rho,\qquad
 U_N=T\Pi_0,\qquad n\in2\mathbb Z+1.
 \tag{9}
\]
Its normalized class
\[
                    e^{\rm pol}_{n,N}=\sigma\mathcal E_{n,N}
                         =2\sigma U_N-i n s_1
 \tag{10}
\]
is a unit for every \(N\ge3\), by the boundary-unit theorem.

Use the exact canonical factorial
\[
 G_N(u)=\left(\frac{2\pi}{N}\right)^u\Gamma(1+u)
 \prod_{m\ge1}
 \frac{\Gamma(Nm+u+1)}
      {\Gamma(Nm-u)(Nm)^{2u+1}},\qquad g_N=\log G_N,
 \tag{11}
\]
on \(-1<\Re u<N\), with its specified logarithm. Put
\[
 z(t)=-2\cos t,\qquad
 \ell_N(t)=\frac{D}{2}-\frac{t}{2\theta},
\]
\[
 V_N(t)=\sigma\left[
 2\cos\theta+\frac{2\sin\theta}{\theta}
          \{g_N'(\ell_N(t))-g_N'(0)\}\right],
 \qquad
 e_{n,N}(t)=2\sigma V_N(t)-i n s_1.
 \tag{12}
\]
The Ward-interpolation theorem proves that \(V_N\) is even,
holomorphic for \(|\Re t|<\pi+\pi/N\), and has precisely the
physical full-Hermite data of \(U_N(z(t))\). Thus (12) represents
(10) inside every original trace.

Let \(\psi=\Gamma'/\Gamma\). There is a unique
\[
 u_*\in(-1/2,0),\qquad \psi(1+u_*)-\psi(1)=-1,
 \qquad p_*=\psi'(1+u_*)>0.
 \tag{13}
\]
Indeed \(\psi'(v)=\sum_{k\ge0}(k+v)^{-2}>0\) for \(v>0\).
The duplication formula gives
\(\psi(1/2)-\psi(1)=-2\log2<-1\), whereas the difference is
zero at \(u=0\). The strict inequality follows, for example, by
integrating \(1/x>1/2\) on \(1<x<2\).

**Proposition.** For each fixed signed odd \(n\), and every
sufficiently large \(N\), \(e_{n,N}\) has a simple zero
\[
 t_{n,N}=
 \pi-\frac{\pi(1+2u_*)}{N}
       -\frac{i n\pi^2}{p_*N^2}+O_n(N^{-3}).
 \tag{14}
\]
It also vanishes at \(-t_{n,N}\). For \(n>0\), the first zero
lies in \(-\pi<\Re t<\pi,\ \Im t<0\); for \(n<0\), its negative
does. Thus both signed odd powers have a zero in the lower
physical window. The assertion holds at both level parities.

**Proof.** On every fixed compact subset of \(\Re u>-1\), the
gamma product gives
\[
 g_N'(u)-g_N'(0)
      =\psi(1+u)-\psi(1)+O_{\rm hol}(N^{-2}).
 \tag{15}
\]
To verify the order directly, its logarithmic derivative is
\[
 g_N'(u)=\log(2\pi/N)+\psi(1+u)
 +\sum_{m\ge1}
 [\psi(Nm+u+1)+\psi(Nm-u)-2\log(Nm)].
 \tag{15a}
\]
In its \(m\)-th summand put \(M=Nm\) and use the uniform expansion
\(\psi(M+a)=\log M+(a-1/2)/M+O_a(M^{-2})\).
The two coefficients of \(M^{-1}\), at \(a=u+1\) and \(a=-u\),
cancel identically. Subtracting the same expression at \(u=0\)
therefore has the summable bound \(O_K(\sum_m(Nm)^{-2})\).
Estimates on a slightly larger compact set and Cauchy's formula
give the holomorphic assertion and its fixed derivatives. This
uses the specified gamma product; there is no freely chosen
periodic interpolation factor.

Set \(t=\pi-\theta(1+2u)\), so \(\ell_N(t)=u\), and write
\[
 f_N(u)=\sigma V_N(\pi-\theta(1+2u)).
\]
Equations (12) and (15) give
\[
 f_N(u)=2+2\{\psi(1+u)-\psi(1)\}+O_{\rm hol}(N^{-2}).
 \tag{16}
\]
Its limiting zero \(u_*\) is simple, with derivative \(2p_*\).
Rouche's theorem on a small fixed disk and a Taylor expansion
therefore solve \(f_N(u)=i n\sin\theta\) uniquely near \(u_*\), with
\[
                 u_{n,N}=u_*+\frac{i n\pi}{2p_*N}
                                      +O_n(N^{-2}).
 \tag{17}
\]
This is exactly \(e_{n,N}(t)=0\). Substitution in \(t(u)\) proves
(14), its simplicity and the asserted side of the real axis.
Evenness gives the second zero. No numerical value of \(u_*\)
or finite-level evaluation is used. \(\square\)

This is a zero of the analytic representative, not of the finite
boundary class at a physical node. In fact
\[
 P_N(z(t))=4\sin^2(\pi\ell_N(t)),
 \tag{18}
\]
so \(P_N(z(t_{n,N}))\ne0\) for all sufficiently large \(N\).
All physical poles remain separate from the new zero.

## 4. The correction that cancels the inverse pole

Let \(J_{n,N}(z)\), of degree below \(N\), be the full Hermite
inverse of (10). On the physical angular strip define
\[
 Q_{n,N}(t)=
 \frac{e_{n,N}(t)J_{n,N}(z(t))-1}{P_N(z(t))}.
 \tag{19}
\]
This is holomorphic at every physical angle. At an ordinary double
spectral node the numerator has zero value and zero first normal.
At the odd simple spectral node \(z=-2,\ t=0\), its zero value
and evenness give the required double angular zero. These are
exactly the denominator's multiplicities, including both preimages
of every ordinary spectral root.

For every actual polynomial spectator \(F_N\), there is an exact
identity of meromorphic differentials:
\[
 \boxed{\quad
 \frac{F_N(z(t))J_{n,N}(z(t))z'(t)}{P_N(z(t))}\,dt
 =
 \frac{F_N(z(t))z'(t)}{e_{n,N}(t)P_N(z(t))}\,dt
 +\frac{F_N(z(t))Q_{n,N}(t)z'(t)}{e_{n,N}(t)}\,dt .
 \quad}
 \tag{20}
\]
This is (19) rearranged, without truncation. Near the physical
poles the last differential is holomorphic, so reciprocal
substitution gives the correct original residues. At a simple
zero \(t_*\) of \(e_{n,N}\) away from the physical poles, however,
\[
 Q_{n,N}(t_*)=-\frac1{P_N(z(t_*))}.
 \tag{21}
\]
The two right-hand residues in (20) are therefore exactly opposite:
\[
 \frac{F_N(z(t_*))z'(t_*)}
      {e_{n,N}'(t_*)P_N(z(t_*))},
 \qquad
 -\frac{F_N(z(t_*))z'(t_*)}
       {e_{n,N}'(t_*)P_N(z(t_*))}.
 \tag{22}
\]
The polynomial inverse on the left has no pole there.

The full angular physical residue cycle contains one small positive
circle around each of its \(N\) logarithmic nodes. Its trace
prefactor is \(\eta N^2/(4\pi i)\): the angular covering counts
each spectral residue twice, including the local degree two at the
odd simple node. Thus crossing a single new pole in the first
right-hand differential of (20) contributes, with the chosen
orientation, exactly
\[
 \frac{\eta N^2}{2}\,
 \frac{z'(t_*)}{e_{n,N}'(t_*)P_N(z(t_*))}
                         F_N(z(t_*)).
 \tag{23}
\]
Any original crossing scalars multiply this identity unchanged.

This coefficient need not be small. At \(t_*=t_{n,N}\), the
preceding proof gives
\[
 z'(t_{n,N})=\frac{2\pi(1+2u_*)}{N}+O_n(N^{-2}),\qquad
 e_{n,N}'(t_{n,N})=-\frac{2Np_*}{\pi}+O_n(1),
\]
\[
 P_N(z(t_{n,N}))=4\sin^2(\pi u_*)+O_n(N^{-1}).
\]
The coefficient in (23), divided by \(\eta\), consequently tends to
\[
                  -\frac{\pi^2(1+2u_*)}
                    {8p_*\sin^2(\pi u_*)}\ne0.
 \tag{24}
\]
At \(-t_{n,N}\), both \(z'\) and \(e_{n,N}'\) change sign, so the
coefficient is the same. For a general \(N\)-dependent exterior,
(23) retains its actual value \(F_N(z(t_*))\); no bound on that
value is inferred here.

## 5. Consequence for coherent transport

Equations (3), (7)--(8), and (20) are exact source identities.
In the finite algebra, inverse-current transport inserts the
inverse coupon and retains its shifted spectator. In the analytic
residue representation it also retains the Hermite correction,
or the equivalent residues when reciprocal poles are crossed.

The zero in (14) rules out treating the specific representative
(12) of this algebraic unit as a zero-free multiplier on the whole
lower physical window.
It does not rule out a contour avoiding its zeros, or a coherent
deformation of the sum in (20); the correction cancels the displayed
pole exactly. What remains unproved for arbitrary short components
is a comparison of the complete corrected source cycle with its
geometric relative cycle, including the exterior values in (23)
and the other Ward currents. A finite inverse-jet bound supplies
neither that comparison nor the original scalar's geometric
coefficient.

## 6. Direct sources and written verification

The following complete written sources were read, their directly used
implications checked, and their hashes verified. Computational
appendices in those sources are not used.

| Source | Direct implication | SHA256 |
|---|---|---|
| [Endpoint boundary unit](research_endpoint_matching_boundary_unit.md) | Actual matching class is a full-Hermite unit and its inverse has polynomial mixed-normal bound | ce79146b4a69206ec3daef0f6cd6db73ac2fc99ad88f61499b58b67bdbc6889f |
| [Grouped currents](research_grouped_endpoint_current_matchings.md) | Exact contraction before the exterior; singleton odd monomer (9) | 4047782f665e9e6631e73aac42d55057d6f3cd5ae1e813d89111a0a5caaa21bb |
| [Logarithmic contour transport](research_gaussian_logarithmic_contour_transport.md) | Original residue normalization, differential-weighted spectator shift, full quotient descent and four-circle Ward identity | e7d62f6630dec31ac6c87f75baf1ff707ed7af9221ac4c5199549cdd4ee7f36f |
| [Ward interpolation](research_odd_ward_logarithmic_factorial.md) | Exact even analytic representative with all physical normals and its original strip | 63ae4693846f00a9b843b98b423959964a8ccb3a72dc8ee0fc1ac36b69f3d4b8 |
| [Canonical factorial](research_exact_cyclotomic_factorial.md) | Specified gamma product and its locally normally convergent logarithmic derivative | 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b |

All deductions are written residue identities and analytic estimates.
No mathematical execution, numerical evidence, or tests are used.
