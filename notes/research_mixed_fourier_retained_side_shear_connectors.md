# Uniform finite-source bounds on retained-side shear connectors

Research deduction, 7 November 2026. Exact cyclotomic factorial
remainders make the infinite-height shear estimate uniform in the
level. Applied to the diagonal residue fibers, this pays their
retained-side connectors from the already proved real-cut gaps.
The remaining connector at outgoing real coordinate \(9/20\)
keeps its original finite source and is not bounded here.

The same finite-height-to-tail estimate also applies to the
original upper retained alias with a strictly negative, fixed
total imaginary part. That application has no shifted-chart
poles and does not require a triangular support condition.
Its initial rate still has to be controlled. No numerical
evaluation, replay or new stationary reference is used.

## 1. The exact source along either shear

Keep the original joint row and cardinal from
[the joint global chart](research_mixed_fourier_right_cap_joint_global_chart.md):
\[
\begin{split}
 T_N(s,q)&=e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+q)
                  E_N(a)E_N(q)E_N(s)^3\widehat f_N(q;y),\\
 \widehat f_N(q;y)&=\frac{e^{-\pi i(N-1)y}}N
 e^{2\pi iNyq}\Pi_N(1-y-1/N)E_N(q-y).
\end{split}
\tag{1}
\]
Write \(a=x+ih_a\), \(y=\xi+i\upsilon\). All incoming
parameters and the allocation \(\eta\in\{0,1\}\) are their
original ones. In particular
\[
 x\in[11/50,9/20],\quad |h_a|\le.108,\quad
 .18299<\xi<.18301,\quad .07871<\upsilon<.07873.
\tag{2}
\]
The multiplier \(|d_N(X)|^{\eta/2}\) stays outside every
identity below. It is never divided out.

Put
\[
 s_H=u+iH,\qquad q_H=z-i(H+b),\qquad
 A_N(H)=e^{2\pi iNs_H}T_N(s_H,q_H).
\tag{3}
\]
For the uniform estimates it is enough to allow
\[
 3/25\le u\le1/2,\qquad 9/20\le z\le1,\qquad
 0\le b\le.102,\qquad H\ge1.
\tag{4}
\]
The shared numerator \(\Pi_N(s_H+q_H)=\Pi_N(u+z-ib)\)
is constant along this motion. We use (3) in either of
the following source domains:

- \(b=0\), \(u+z=\ell/N\), \(1\le\ell<N\), so that this
  numerator is the exact physical \(P_\ell\);
- \(b\) lies in a fixed compact subinterval of \((0,.102]\).
  The original lower-half-plane continuation then applies
  to the shared numerator for every \(u+z\) in (4),
  including \(u+z\ge1\).

The second case is the original, unshifted upper-alias
shear. No physical support condition is imposed off-grid.
The numerator \(s_H+a\) and the reciprocal arguments \(s_H\)
and \(q_H-y\) have real parts strictly between zero and one.
The reciprocal at \(q_H\) uses the same lower-half-plane
continuation at \(z=1\); this is \(1/\Pi_N(q_H)\) there,
with no zero or pole. All these arguments are nonreal for
\(H\ge1\).

## 2. An exact slope with a remainder uniform in the level

Use the exact lower-half-plane remainder
\(\mathcal E_N(w)\) and reflection identity from
[the factorial alias proof](research_mixed_fourier_factorial_alias_elimination.md),
equations (2), (3) and (5). Define
\[
\begin{split}
 R_N(H)={}&\overline{\mathcal E_N(\overline{s_H+a})}
      -3\overline{\mathcal E_N(\overline{s_H})}\\
      &-\mathcal E_N(q_H)-\mathcal E_N(q_H-y),\\
 \Lambda_N(u)&=2\pi\{N(2u-\xi)+1\}.
\end{split}
\tag{5}
\]
Every argument of \(\mathcal E_N\) in (5) is in its open
lower half-plane. Substitution in (1) gives an exact
modulus identity
\[
              |A_N(H)|=C_N\,e^{-\Lambda_N(u)H+\Re R_N(H)},
                    \qquad H\ge1,
\tag{6}
\]
where \(C_N\) is independent of \(H\). It contains the
unchanged factors \(P_\ell\), or \(\Pi_N(u+z-ib)\),
the incoming reciprocal, the cardinal normalization and
all original finite phases. Its size is not assumed bounded
independently of \(N\).

For clarity, the height coefficients from the upper factorials
and the elementary exponentials in (1) are respectively
\[
\begin{split}
 &\pi\{N(2u+2x-1)+1\}
       -3\pi\{N(2u-1)+1\},\\
 &-2\pi Nx+2\pi N\xi-2\pi N.
\end{split}
\]
Their sum is \(-\Lambda_N(u)\). Thus the finite \(+1\)
in (5) is retained. The shift \(b\), the incoming height
and the outgoing real coordinate affect only \(C_N\)
and the remainders, not this slope. In particular,
\[
                    \Lambda_N(u)>\pi N/10+2\pi
\tag{7}
\]
on (2), (4).

Here is an explicit uniform control of the remainders.
For \(H\ge1\), set
\[
 r_H=e^{-2\pi(H-.108)},\qquad
 \psi(H)=\frac{H+3}{2}\frac{r_H^2}{1-r_H^2}
                      +\frac12\frac{r_H}{1-r_H}.
\tag{8}
\]
Each lower-half-plane argument \(w\) in (5) satisfies
\(|w|\le H+2\) and \(|e^{-2\pi iw}|\le r_H<1\).
The exact remainder bound, \(N\ge2\), and \(r_H^N\le r_H^2\)
therefore imply
\[
       \frac{|\mathcal E_N(w)|}{N}\le\psi(H),
       \qquad \frac{|R_N(H)|}{N}\le6\psi(H).
\tag{9}
\]
The two summands in (8) decrease on \(H\ge1\).
For the first, its logarithmic derivative is
\(1/(H+3)-4\pi/(1-r_H^2)<0\); the second is immediate.
Consequently \(\psi(H)\downarrow0\), with no dependence
on \(N\).

**Lemma 1.** For any fixed \(H_1\ge1\) and all \(H\ge H_1\),
\[
 |A_N(H)|\le |A_N(H_1)|
       \exp\{12N\psi(H_1)-\Lambda_N(u)(H-H_1)\}.
\tag{10}
\]
In particular
\[
 \int_{H_1}^{\infty}|A_N(H)|\,dH
 \le\frac{|A_N(H_1)|e^{12N\psi(H_1)}}{\Lambda_N(u)}.
\tag{11}
\]
Equations (10)--(11) follow by subtracting the two exact
exponents in (6). Thus no uncontrolled fixed-\(N\) asymptotic
constant is promoted to a uniform one. The same inequalities
hold after multiplying by the original incoming halfweight,
including at its zeros.

For the exact upper-alias integrand
\[
 \frac{e^{2\pi iNs_H}}{1-e^{2\pi iNs_H}}T_N(s_H,q_H),
\tag{12}
\]
one retains its denominator. On \(H\ge H_1\ge1\), its
inverse has modulus at most
\((1-e^{-4\pi H_1})^{-1}\), uniformly in \(N\ge2\).
Thus (11) also controls its tail with this additional
constant and the value \(|A_N(H_1)|\). At a half-grid
retained side the denominator is exactly
\(1+e^{-2\pi NH}\). No outgoing Fourier multiplier
present in another current is discarded by (10)--(12).

## 3. Calibrating the retained-side residue fibers

Use the cuts \(\sigma_\pm\), the functions \(D_{\ell,N}\)
and the plane \(B_\eta(x)\) of
[the diagonal-residue source](research_mixed_fourier_right_cap_diagonal_residue_source.md).
Put \(h=-h_q\in[.001,.102]\). On a retained-side fiber,
\[
 u=\sigma_-\ \hbox{or}\ \sigma_+,\qquad
 z=\ell/N-u\ge9/20,\qquad q_H=z-iH,\quad H\ge h.
\tag{13}
\]
Its exact source is
\[
 J_{\ell,N}(z-iH)
      :=e^{-2\pi iN(z-iH)}D_{\ell,N}(z-iH).
\tag{14}
\]
Since \(s_H+q_H=\ell/N\), (14) equals \(A_N(H)\)
exactly, not just in modulus. Its allocated phase is
\[
 \mathcal P_\eta(H)
   =\Re F_\eta(u+iH,a,z-iH)-2\pi H.
\tag{15}
\]

At the limiting cuts \(u=1/8,1/2\), the relative-height
bound of the diagonal-source note and the actual cut
estimates in
[the nonpositive-correction theorem](research_mixed_fourier_right_cap_nonpositive_index_corrections.md)
give
\[
\begin{split}
 \mathcal P_\eta(h)
 &<\Re F_\eta(u,a,z-ih)-13\pi h/200\\
 &<B_\eta(x)-1/35000-13\pi h/200.
\end{split}
\tag{16}
\]
The same conclusion with the last reserve halved holds at
the actual half-grid cuts for all sufficiently large \(N\),
uniformly in the layers. To justify this without a derivative
at the total-index endpoint, first use the relative-height
argument at the actual \(u\). Its shared logarithm has
argument greater than \(-\pi/2\), uniformly as
\(\ell/N\to1\); the other argument bounds have strict room.
Only then compare the resulting real-retained profile to
its limiting cut. That profile has shared height \(-h\le-.001\),
so this \(O(1/N)\) real displacement lies in a common regular
compact set. The spare \(h\ge.001\) in (16) pays it.

The
[uniform shear theorem](research_mixed_fourier_diagonal_shear_monotonicity.md)
gives \(\mathcal P_\eta'(H)<-1/20\) on the limiting
supported interval. At the actual half-grid cuts it gives
the weaker uniform bound
\[
       \mathcal P_\eta(H)\le
       B_\eta(x)-1/35000-(H-h)/40,\qquad H\ge h.
\tag{17}
\]
Indeed the total-index derivative cancels before this estimate;
the remaining argument expression is continuous on a fixed
neighborhood of the cut ranges, with \(r=e^{-2\pi H}\in[0,1]\).
The support condition keeps the outgoing real argument away
from one at these cuts. Thus its strict \(1/20\) margin is
stable under the half-grid displacement, uniformly in \(H\).

**Theorem 2.** The sum of the absolute retained-side connector
integrals, with their original outgoing coefficient \(N\),
satisfies, for all sufficiently large \(N\) of either parity,
\[
 |d_N(X)|^{\eta/2}\,
 N\sum_{\text{retained-side endpoints}}
       \int_h^\infty |J_{\ell,N}(z-iH)|\,dH
       \le e^{N(B_\eta(x)-1/140000)}.
\tag{18}
\]
There are at most \(2(N-1)\) endpoints in this sum.

For the proof fix \(\epsilon=1/(4\cdot35000)\).
Choose one \(H_1\ge1\) with \(12\psi(H_1)<\epsilon\).
On the fixed compact interval \(h\le H\le H_1\), the
original source upper bounds and (17) give
\[
 |d_N(X)|^{\eta/2}|J_{\ell,N}(z-iH)|
 \le C_\epsilon N^{A_\epsilon}
                  e^{N(B_\eta(x)-1/35000+\epsilon)}.
\tag{19}
\]
The physical numerator is kept as \(P_\ell\); its uniform
\(N J(\ell/N)+O(\log N)\) bound includes \(\ell=N-1\).
All moving factors lie in regular fixed-height strips.
The incoming weight uses its original rate-tolerance bound;
no tolerance-free polynomial assertion is needed for it.

Use (19) at \(H_1\) in (11) for the infinite end. This loses
at most the further \(\epsilon\), uniformly in \(N,\ell\).
The remaining finite interval, the at most \(2(N-1)\)
layers, and the outside \(N\) cost only a fixed polynomial.
Absorbing that polynomial leaves the gap \(1/(4\cdot35000)\)
in (18). The height \(H_1\) was fixed before allowing \(N\)
to grow. Fixed-\(N\) convergence and this uniform estimate
are distinct steps.

## 4. Exact transport of every residue fiber

Take the entire outgoing right interval
\([c,\beta_N]\), \(c=9/20\). For a nonempty residue fiber put
\[
 a_{\ell,N}=\max(c,\ell/N-\sigma_+),\qquad
 b_{\ell,N}=\ell/N-\sigma_-.
\tag{20}
\]
For sufficiently large \(N\), \(b_{\ell,N}<\beta_N\)
because \(\ell<N\) and \(\sigma_->1/(2N)\).
Hence (20) is exactly the inventory obtained by intersecting
the shifted-pole fiber with the full right interval.
The endpoints do not create a physical layer \(\ell=N\).

The function \(J_{\ell,N}(q)\) is holomorphic on and below
this fiber: \(s=\ell/N-q\) has its central real part, all
reciprocal real parts are below one, and the shared numerator
is the fixed nonzero \(P_\ell\). The poles of the shifted
chart have already contributed the exact residues (14);
they are not crossed a second time in this original-layer
continuation.

Cauchy's theorem, retaining both vertical sides, gives
\[
\begin{split}
 \int_{a_{\ell,N}}^{b_{\ell,N}}J_{\ell,N}(z-ih)\,dz
 ={}&\int_{a_{\ell,N}}^{b_{\ell,N}}J_{\ell,N}(z-iH_1)\,dz\\
 &+i\int_h^{H_1}
  \{J_{\ell,N}(b_{\ell,N}-iH)
                  -J_{\ell,N}(a_{\ell,N}-iH)\}\,dH .
\end{split}
\tag{21}
\]
Lemma 1 makes the lower horizontal integral tend to zero
as \(H_1\to\infty\), at fixed \(N\), and makes both
vertical sides absolutely convergent. The estimate is
uniform on the finite real fiber. Therefore the original
residue current is exactly
\[
 \mathcal R_N
 =iN\sum_{\ell:\ a_{\ell,N}<b_{\ell,N}}
 \int_h^\infty
 \{J_{\ell,N}(b_{\ell,N}-iH)
                  -J_{\ell,N}(a_{\ell,N}-iH)\}\,dH .
\tag{22}
\]
This sign agrees with the outgoing coefficient in the
shifted-current identity.

The endpoint \(b_{\ell,N}\) always has retained coordinate
\(\sigma_-\). If \(a_{\ell,N}=\ell/N-\sigma_+\), it also
is a paid retained-side endpoint. Theorem 2 bounds the
sum of all these terms. The remaining part is precisely
\[
 \boxed{\quad
 \mathcal C_N^{\,c}=
 -iN\!\!\sum_{\substack{\ell<N\\
             \sigma_-<\ell/N-c<\sigma_+}}
       \int_h^\infty
        e^{-2\pi iN(c-iH)}
               D_{\ell,N}(c-iH)\,dH .
 \quad}
\tag{23}
\]
Endpoint equalities may be assigned to the retained-side
term; they do not change the original fiber integral.
Thus \(\mathcal R_N-\mathcal C_N^{\,c}\) has the
allocated bound (18).

The retained real coordinate in (23) is free. Its initial
value is not a real-cut profile. Neither the shear decay nor
absolute convergence assigns it the calibrated bound
\(B_\eta\). Formula (23) preserves that outgoing-cut
connector, the full original cardinal, the outgoing harmonic,
all residue layers and the incoming finite halfweight.
It is the remaining term of this transport, not an omitted
error. The original, strictly negative-total-height
upper-alias shear has the uniform tail estimate of
Lemma 1, but requires its own current assembly and initial
connector comparisons.

## 5. Fixed starting heights, including the complete high cap

The exact tail argument permits bounded starting offsets of
both heights. This includes a high retained cap, and also a
retained path at the original negative critical height.
Let
\[
\begin{gathered}
 -1/5\le v_0\le5/4,\qquad -.102\le k_0\le-.001,\qquad
 -1/100\le z\le1,\qquad 3/25\le u\le1/2,\\
 s_t=u+i(v_0+t),\qquad q_t=z+i(k_0-t),\qquad
 A_N^{\rm off}(t)=e^{2\pi iNs_t}T_N(s_t,q_t),\qquad t\ge1.
\end{gathered}
\tag{24}
\]
The shared argument \(s_t+q_t=u+z+i(v_0+k_0)\) is fixed,
with positive real part. Its original numerator is holomorphic
at every such point; a possible positive-support zero is
retained multiplicatively. No division by that numerator
is made. The outgoing reciprocal factors are evaluated in
their lower half-plane. The
[global lower-half-plane continuation](research_lower_half_factorial_continuation.md)
and the original reciprocal identity apply also when
\(\Re q_t\) or \(\Re(q_t-y)\) is negative. In particular
\(z=\alpha_N=-1/(2N)\) is covered for all sufficiently
large \(N\).

Replace \(s_H,q_H\) by \(s_t,q_t\) in (5). The resulting
remainder \(R_N^{\rm off}(t)\) gives the same exact slope:
\[
 |A_N^{\rm off}(t)|
   =C_N^{\rm off}
          e^{-\Lambda_N(u)t+\Re R_N^{\rm off}(t)}.
\tag{25}
\]
The coefficient \(C_N^{\rm off}\) may be zero if the fixed
numerator vanishes. The equation and all the ensuing upper
bounds remain valid in that case.

Each lower-half-plane remainder argument has imaginary
depth at least \(t-77/250\) and modulus at most \(t+3\).
The worst possible upper-factorial depth is
\(t+v_0+h_a\ge t-.2-.108=t-77/250\).
The outgoing lower depths are larger. Hence put
\[
 r_t^{\rm off}=e^{-2\pi(t-77/250)},\qquad
 \psi_{\rm off}(t)=
       \frac{t+4}{2}\frac{(r_t^{\rm off})^2}
                              {1-(r_t^{\rm off})^2}
       +\frac12\frac{r_t^{\rm off}}{1-r_t^{\rm off}}.
\tag{26}
\]
Exactly the proof of (9) gives
\[
 |R_N^{\rm off}(t)|\le6N\psi_{\rm off}(t),
          \qquad \psi_{\rm off}(t)\downarrow0\quad(t\ge1).
\tag{27}
\]
The first term has logarithmic derivative
\(1/(t+4)-4\pi/[1-(r_t^{\rm off})^2]<0\).

**Lemma 3.** For every fixed \(T_1\ge1\),
\[
\begin{split}
 |A_N^{\rm off}(t)|
 &\le |A_N^{\rm off}(T_1)|
 e^{12N\psi_{\rm off}(T_1)-\Lambda_N(u)(t-T_1)}
                                     &&(t\ge T_1),\\
 \int_{T_1}^\infty|A_N^{\rm off}(t)|\,dt
 &\le\frac{|A_N^{\rm off}(T_1)|
                e^{12N\psi_{\rm off}(T_1)}}{\Lambda_N(u)}.
\end{split}
\tag{28}
\]
For the exact upper kernel, additionally retain
\[
 \left|1-e^{2\pi iNs_t}\right|^{-1}
       \le\left(1-e^{-4\pi(T_1-1/5)}\right)^{-1},
                       \qquad t\ge T_1.
\tag{29}
\]
These bounds are uniform in all the offsets (24).
They include arbitrary compact fixed total imaginary
height, not only negative total height. The original
finite halfweight can multiply both sides unchanged.

The same observation controls a lower outgoing kernel
when one occurs in an exact transformed current. With
\(Z_{q_t}=e^{-2\pi iNq_t}\), one has exactly
\[
 \frac{Z_{q_t}}{1-Z_{q_t}}\,T_N(s_t,q_t)
 =\frac{e^{-2\pi iN(s_t+q_t)}}{1-Z_{q_t}}\,
                              A_N^{\rm off}(t).
\tag{30}
\]
The numerator on the right is constant along the shear.
It remains in the source; it is not replaced by one.
The denominator is zero-free since \(\Im q_t<0\).
Thus (28) also supplies the infinite end of (30), with
this exact fixed multiplier and its bounded denominator.
This is a tail estimate, not an assertion that the fixed
multiplier has a favorable exponential rate.

## 6. Infinite transport of the original positive retained current

Use the original upper-current arch, its four oriented faces
and their exact identity from
[the coupled original-current transport](research_mixed_fourier_original_upper_shear_transport.md).
There \(c=9/20\), \(d=\beta_N\), \(h_0=-h_q/2\), and
\[
 \Gamma(h_0):
 \sigma_-\longrightarrow\sigma_-+ih_0
 \longrightarrow\sigma_++ih_0\longrightarrow\sigma_+ .
\]
Write \(\mathcal I_N(T)\), \(\mathcal S_{N,A/B}(T)\)
and \(\mathcal Q_{N,c/d}(T)\) exactly as in that note.
In particular each integral retains the outside \(N^2\)
and the cardinal \(1/N\) inside the row.

On the translated arch, (24) has
\(0\le v_0\le h_0\), \(k_0=h_q\), and shared height
\(v_0+h_q<0\). Lemma 3 proves
\[
                  \lim_{T\to\infty}\mathcal I_N(T)=0
\tag{31}
\]
at each fixed level. It also proves absolute convergence
of the four face integrals. At a fixed level the real
domains and the starting arch are compact, so the exact
constant in (25) is bounded there. For large \(N\), (7)
gives the required positive slope. At every smaller
nonempty level use the exact finite correction instead:
\[
 N(2u-\xi)+1\ge2\lceil N/8\rceil-N\xi
                         \ge N(1/4-\xi)>0
                  \qquad(u\ge\sigma_-).
\tag{31a}
\]
The exact fixed-level factorial expansion remains valid
on that compact real interval, even if \(u<3/25\).
At \(N=2\) the central source is empty. At finite \(t\),
the original holomorphy and half-grid endpoints exclude
kernel poles.

The retained faces begin at the real cuts, whose original
gap is \(\delta_*=1/35000\). Their paid phases decrease
along the support-free original shear. These statements
and their finite-source normalization are proved in
Sections 3--4 of the cited transport note.

For the left outgoing face, its exact path replacement
uses \(\Gamma(5/4)+it\), with the same endpoints as
\(\Gamma(h_0)+it\). Every initial high-cap profile has
gap at least \(\delta_*\), and its paid phase decreases
by at least \(t/3\), as proved in Section 5 there.
This replacement is made before taking the absolute
value of the complete outgoing-face integrand.
It does not assert a pointwise bound on the small arch.
All offsets of that high cap belong to (24).

Choose one fixed \(T_1\) with
\(12\psi_{\rm off}(T_1)<\delta_*/8\).
On \(0\le t\le T_1\), use the original compact finite-source
bounds with tolerance less than \(\delta_*/8\) and the
just described phase comparisons. On \(t\ge T_1\), apply
(28)--(29) to those same source profiles at \(T_1\).
The half-grid displacement, fixed contour lengths, outside
powers of \(N\) and the finite number of pieces are absorbed
with the remaining reserve. This proves, at both parities,
\[
\begin{split}
 |d_N(X)|^{\eta/2}N^2
 \Bigg[&
 \sum_{e=A,B}\int_0^\infty\int_c^{\beta_N}
 \left|\mathcal F_N(e+it,z+i(h_q-t))\right|\,dz\,dt\\
 &+\int_0^\infty
 \left|\int_{\Gamma(h_0)}
        \mathcal F_N(s+it,c+i(h_q-t))\,ds\right|dt
 \Bigg]
 \le e^{N(B_\eta(x)-1/140000)} .
\end{split}
\tag{32}
\]
Here \(\mathcal F_N=K_N^+T_N\) and \(A=\sigma_-\),
\(B=\sigma_+\) only in the endpoint sum. The upper bound
for the second line is obtained by integrating the
absolute profiles on the replacement high arch.

Consequently the exact finite-height transport identity
has the convergent infinite-height form
\[
 \mathcal I_N(0)=
 -i\mathcal S_{N,B}(\infty)+i\mathcal S_{N,A}(\infty)
 +i\mathcal Q_{N,\beta_N}(\infty)
 -i\mathcal Q_{N,c}(\infty),
\tag{33}
\]
and the original upper-plus-positive-retained-side
contribution differs from \(i\mathcal Q_{N,\beta_N}(\infty)\)
by at most the allocated bound (32).

The right outgoing connector is absolutely convergent,
but (32) assigns it no calibrated rate. It keeps its
whole retained arch and the original cardinal lift.
In particular this conclusion neither drops that connector
nor replaces it by the previously paid right-return current.
The residue transport (22)--(23) and the original-chart
transport (33) are separate exact representations; their
correction terms are not combined or counted twice.
