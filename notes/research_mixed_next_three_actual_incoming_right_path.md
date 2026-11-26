# The full right incoming path at the actual cap-343 heights

Private finite-source proof, 8 November 2026. The complete first
right horizontal segment and its subsequent oriented corner are
bounded with the whole next own-three kernel attached, for actual
complete words beginning \(343\) of length at least five. The final
real incoming arc is included as well. The proof replaces the
radius-dependent inputs in the earlier argument: its last
profile is now controlled by the correlated heights, and its upper
physical rows are controlled individually by joint transport.

This draft awaits full independent source and proof reviews. Its
bounded-prefix input is the separately frozen and reviewed
actual-height theorem. No mathematical numerical evaluation or
modification of an earlier frozen source is used. No remaining
shared-variable Fourier contour is estimated here.

## 1. Actual reference, finite source and paths

Keep exactly the actual ordinary-next reference of
[actual central completion](research_mixed_next_three_actual_central_completion.md):
a complete word in the original powers three and four, beginning
\(343\), with length \(m\ge5\). Write
\[
 (a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3),\qquad
 A=\Re a_*,\quad\alpha=\Re y_*,\quad P=[11/50,9/20].
 \tag{1}
\]
All five heights \(h_a,h_s,h_y,h_t,h_z\) are held at their actual
values. The outside parameter remains the actual \(b=s_4\); no
independent substitution for the suffix or its critical point is made.
The inherited domains give
\[
\begin{gathered}
 .278\le A\le.391,\quad .24<\alpha<.36,\quad -.072<h_a<0,\\
 -.102<h_s,h_y<-.001,\qquad -.03<h_t,h_z<.02,\\
 y=q+ih_y,\quad 0\le q\le q_0=11/50,\qquad
 z=u+ih_z,\quad u\in P.
\end{gathered}                                                    \tag{2}
\]
The [correlated height theorem](research_mixed_cap_343_correlated_height_bounds.md)
and its separate interior-window refinement supply
\[
 \frac7{10}<R=e^{2\pi h_y}<\frac{41}{50},\qquad
 r_s=e^{2\pi h_s}>\frac45R,\qquad
 \rho=e^{2\pi h_z}>\frac45,
 \quad \rho<\frac{43}{28}.
 \tag{3}
\]
The first two inequalities already apply at \(m\ge4\), but the
height refinement at vertex three used in (2)--(3) requires
\(3\le m-2\). Thus this note does not include length four or the
terminal word \(343\).

Put \(r=e^{-2\pi i/N}\), \(D=N-1\),
\(P_j=(r;r)_j\), \(p_j(V)=(rV;r)_j\), and
\(X=e^{-2\pi ia},Y=e^{-2\pi iy},Z=e^{-2\pi iz}\). Retain
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{k=0}^{D}H_N(w,r^{-k})p_k(X)/P_k,\\
 C_{\beta,N}(V,W)&=\sum_{j=0}^{D}
                  \frac{V^{-j}p_j(V)p_j(W)}{P_j^{2+\beta}},\\
 D_N(a)&=U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{0,N}(Y,Z).
\end{split}                                                     \tag{4}
\]
Here \(H_N\) is the complete original endpoint polynomial, with
its ordinary color and normalization. The original polynomial
\(d_N\) has degree at most \(D\) and satisfies
\(d_N(r^b)=P_b^{-1}\). It occurs once, with its forcing retained.
There is no selected \(Y^{-N}\) and no outgoing halfweight.

Set \(a_L=1/2+ih_a\) and define the oriented paths
\[
\begin{split}
 \Gamma_H&=[9/20+ih_a,a_L],\\
 \Gamma_C&=[a_L,1/2]\cup[1/2,7/10],\\
 \widetilde\Gamma_C&=[a_L,7/10+ih_a]
                         \cup[7/10+ih_a,7/10],\\
 \Gamma_F&=[7/10,1],\qquad
 \Gamma_R=\Gamma_H\cup\Gamma_C\cup\Gamma_F.
\end{split}                                                     \tag{5}
\]
Every interval is oriented from its first endpoint to its second.
Let \(\Lambda_{123}(z)\) be the unchanged original affine plane
in [complete lower plateau, equation (6)](research_mixed_next_complete_lower_plateau.md).
For this own type its value at \(z_*\) is
\(\Re\mathcal P_0^+(-2,z_*)\).

**Theorem.** Uniformly on the actual family (1)--(3), for all real
ordinary colors \(w\in[-2,2]\) and sufficiently large levels of
both parities,
\[
\begin{split}
 |D_N(a)|&\le CN^B e^{N\{\Lambda_{123}(z)-10^{-11}\}},
                  &&a\in\Gamma_H,\\
 |D_N(a)|&\le CN^B e^{N\{\Lambda_{123}(z)-10^{-10}\}},
                  &&a\in\widetilde\Gamma_C,\\
 |D_N(a)|&\le CN^B e^{N\{\Lambda_{123}(z)-1/200\}},
                  &&a\in\Gamma_F.
\end{split}                                                     \tag{6}
\]
Consequently the whole original right path satisfies
\[
 \boxed{\quad
 \left|N\int_{\Gamma_R}D_N(a)\,da\right|
       \le CN^B e^{N\{\Lambda_{123}(z)-10^{-11}\}}.
 \quad}                                                         \tag{7}
\]
The corner is used as its combined oriented integral. No separate
absolute estimate for either old side of \(\Gamma_C\) is asserted.
No outside-neighborhood or normalized local-jet assertion is needed
for this theorem.

## 2. Raw alternatives and the precise replacements

The [actual bounded-prefix theorem](research_mixed_next_three_actual_bounded_prefix.md)
applies to (1)--(3): a preceding factor of rate at most
\[
                         B_0=2383/1500                       \tag{8}
\]
with every prescribed extra tolerance can be multiplied by the
complete \(d_N(Y)C_{0,N}(Y,Z)\), with deficit \(1/200\) below
\(\Lambda_{123}\). This is an absolute attachment; the preceding
factor need not be holomorphic or a complete conditional sum.

For \(a=x+ih_a\), \(9/20\le x\le1/2\), take the first cuts
\[
 c=1/20,\quad L_N=\lfloor N/20\rfloor+1,\quad
 M_N=\lceil N/2\rceil,\quad b=1/2.
 \tag{9}
\]
The full disk estimates of
[right horizontal, Section 2](research_mixed_next_lower_left_incoming_right_horizontal.md)
give the following complete cap-times-first rates:
\[
\begin{array}{c|c}
 \text{positive physical rows }0\le i<L_N
           \text{ and the real cut }c&3111/2000<B_0,\\
 \text{first last alternative }\delta_a=-2\pi h_a
                                      &11099/7000<B_0.
\end{array}                                                     \tag{10}
\]
These proofs use only \(|Y|\le1\), the folded incoming modulus
\(<13/5<e\), the numerator bound \(2\), and the uniform
sine-factorial bound, with the exact zero row retained. Their
complete cap ceiling is \(1133/1000\). The last inequality in
(10) follows from \(\delta_a<18\pi/125\); its strict difference
from \(B_0\) is \(13/4200\). Neither estimate used the next own
flag or the old restriction \(R\le7/10\). Thus (8) pays them
against the whole next sum.

The earlier
[deeper-radius horizontal proof](research_mixed_next_three_deep_radius_right_horizontal.md)
used \(R\le7/10\) at three places: its raw attachment, its
first-main by next-last transport, and its scalar upper-row
envelope (21). We replace the first by (8), the second by (3)
and the correlated transport below, and the third by individual
joint upper-row comparisons. In particular its scalar envelope
(21) is not imported on the actual radius range.

## 3. Uniform calibration of every next profile

Keep the original phases and full shared allocation
\[
\begin{split}
 Q_\beta(v;b,c)&=g(b+v)+g(c+v)-(2+\beta)g(v)
                         -g(b)-g(c)+2\pi ibv,\\
 F_1&=Q_1(s;a,y)-g(y)/2,\qquad
 F_2=Q_0(t;y,z)-g(y)/2,\\
 B_U(x)&=\Re T_0(a_*)-\Re p_L(x-A)-\kappa_0(x-A)^2,
                      \qquad\kappa_0=1/2500000.
\end{split}                                                     \tag{11}
\]
Here \(p_L=Q_{1,a}(s_*;a_*,y_*)\), and \(g,T_0\) keep their
original absolute constants and logarithmic branches.
The complete all-real cap has supporting rate \(B_U(x)\) through
\(x=1/2\), by the original right-tail source. Its retained loss is
\[
 \Delta(x):=\kappa_0(x-A)^2
       \ge\frac{3481}{2500000000000}>10^{-9}.
 \tag{12}
\]
Write the exact physical rate and last rate of the next kernel as
\[
\begin{split}
 E_0(t;y,z)&=\int_0^t\log|1-Ye^{-2\pi ib}|\,db
       +\int_0^t\log|1-Ze^{-2\pi ib}|\,db-2J(t)-t\log R,\\
 L_0&=-\log R+\log_+\rho=E_0(1;y,z).
\end{split}                                                     \tag{13}
\]
The positive outgoing-height carrier in \(L_0\) is never removed.
Use the full following profile family
\[
\begin{split}
 \mathscr P(y,z)={}&
 \{\Re Q_0(t_R+ih_t;y,z):3/20\le t_R\le1/2\}\\
 &\cup\{E_0(3/20;y,z),E_0(1/2;y,z),L_0\}\\
 &\cup\{E_0(t;y,z):1/2\le t\le1\}.
\end{split}                                                     \tag{14}
\]
Unlike the earlier deeper-radius profile list, this retains every
upper physical rate without a scalar endpoint-maximization claim.

We prove the pointwise calibration
\[
 \boxed{\quad
 B_U(x)+\Re Q_1(s_R+ih_s;a,y)+\varphi-\Re g(y)
       \le\Lambda_{123}(z)-\Delta(x)
 \quad}                                                        \tag{15}
\]
for \(c\le s_R\le1/2\), \(9/20\le x\le1/2\), and every
\(\varphi\in\mathscr P(y,z)\). This statement precedes both
index summations.

### Main and real-cut profiles

The first clipping proof in the deeper-radius horizontal theorem,
Section 3, uses no radius restriction beyond \(1/2<R<1\).
On \(c\le s_R\le1/8\) its exact force increases to \(1/8\):
the incoming modulus exceeds one, the outgoing modulus is at least
\(\cos(\pi s_R)\) times the own modulus, and the own square is
less than \(3/5\). The subsequent two clippings give
\[
                        1/6\le s_R\le5/12.                 \tag{16}
\]
They remain valid through \(x=1/2\); the upper clipping improves
on \(x+s_R\in[13/15,1]\), and \(h_a+h_s<0\) keeps that
main numerator regular. The next own-three lower clipping gives
\(1/6\le t_R\le1/2\) at its unchanged height \(h_t\), allowing
either sign. No own-four upper clipping is imposed on that index.

For \(1/5\le q\le q_0\), the fixed-height supporting argument
in Section 3 of the deeper-radius proof applies unchanged.
Explicitly, with \(V(v,w)=g(v+w)-g(v)-g(w)\), the two allocated
phases are
\[
\begin{split}
 F_1&=V(s,a)+V(s,y)-g(s)-g(y)/2+2\pi ias,\\
 F_2&=V(t,y)+V(t,z)-g(y)/2+2\pi iyt.
\end{split}                                                     \tag{17}
\]
On these straight horizontal reference-to-target segments, each
individual real part lies in \([1/6,1/2]\), and every shifted
sum is below one. The common cotangent determinant theorem gives
negative semidefinite real Hessians, including individual half
faces; it is strict in the interior. The extra own terms have
the correct nonnegative negative-Hessian diagonals, and the chirps
are purely imaginary in this horizontal Hessian. The private
critical equations remove the index tangents. The attached
equation \(T_0'(a_*)+p_L=0\) and the original shared marginal
cancellation leave exactly \(\Lambda_{123}\). Together with
the cap loss, this proves (15) for both main profiles.

For \(0\le q\le1/5\), the joint derivative is exactly
\[
 \exp\partial_q\Re(F_1+F_2)=
 \frac{|1-Rr_s e^{-2\pi i(q+s_R)}|
       |e^{-2\pi h_t}-Re^{-2\pi i(q+t_R)}|}
      {|1-Re^{-2\pi iq}|^3}>1 .                              \tag{18}
\]
The three interval proofs in
[joint profiles, Section 4](research_mixed_next_lower_left_joint_main_profiles.md)
use only the clipped indices, \(R,r_s\in(1/2,1)\), and
\(e^{-2\pi h_t}>13/20\). They are independent of \(x\).
Transport to \(q=1/5\) proves (15) for the remaining main profiles.

At either next real cut \(3/20,1/2\), its real-height version
also increases on \(q\le1/5\). On \([1/5,q_0]\), the exact
joint-profile inequalities are
\[
 U>(23/20)D,\qquad W>(20/23)D^2,
\quad
 \begin{cases}
 D=1+R^2-9R/25,\\
 U=1+R^2/4+13R/20,\\
 W=1+R^2+9R/25.
 \end{cases}                                                  \tag{19}
\]
Thus the derivative stays positive. At \(q_0\), the original
own-three real-cut certificate has deficit \(1/2000\); the cap
loss (12) remains in addition. This proves (15) for both real cuts.

### Last profile and all upper physical profiles

With \(L_0\) attached, the first-main derivative is
\[
 \partial_q\{B_U+\Re Q_1+L_0-\Re g(y)\}
 =\log|1-Rr_s e^{-2\pi i(q+s_R)}|-2\log|1-Y|>1/5000.
 \tag{20}
\]
This is [correlated last transport, Section 2](research_mixed_next_three_correlated_last_row_transport.md),
whose hypotheses are exactly the two correlated inequalities in
(3), and whose derivative does not involve \(x\). At \(q_0\)
the original own-three last certificate is used only for its
strict sign. The first supporting inequality and the cap retain
\(\Delta(x)\). Hence (20) proves (15) for \(L_0\) on the
entire shared interval. No numerical last-row margin is assigned.

Put \(v=1-t\) for an upper physical rate. The following cases
prove (15) for every \(0\le v\le1/2\).

1. If \(v\ge q+1/5\), the exact diagonal derivative with
   \(dq=dv\) is
   \[
   \frac{R|1-Rr_s e^{-2\pi i(q+s_R)}|(2\sin\pi v)^2}
        {|1-Y|^3|1-Ze^{2\pi iv}|}>1.                         \tag{21}
   \]
   The [old-face band](research_mixed_next_own_three_upper_band_old_face.md),
   Sections 3--4, proves this with the full outgoing radius domain
   in (3). None of its multiplier estimates involves \(x\).
   Stop at \(v=1/2\), already paid by the next half profile,
   or at \(q=q_0\), where the original next upper rows reduce
   to the half/last certificates. The cap reserve (12) survives
   at either endpoint.

2. If \(v\ge3/10\) and \(v<q+1/5\), the
   [fixed-shared band](research_mixed_next_own_three_upper_band_fixed_shared.md)
   gives \(\partial_vE_0(1-v)>1/20\). Move at fixed \(q\)
   to \(v=q+1/5\). This is a scalar row comparison independent
   of the first profile, so the preceding case applies.

3. If \(v\le q\), the all-radius comparison in
   [upper-end reduction, Section 2](research_mixed_next_own_three_upper_end_last_reduction.md)
   gives \(E_0(1-v)\le L_0\), with both carriers retained.
   If \(v\le1/5\), the
   [small reflected theorem](research_mixed_next_three_small_reflected_logarithmic_bound.md)
   gives the stronger \(E_0(1-v)\le L_0-v/600\), regardless
   of the ordering of \(q,v\). Its radius hypotheses follow
   from (3). Both cases reduce to (20).

4. The only remaining case has \(q<v<3/10\) and \(v>1/5\).
   For \(q\ge3/20\), Sections 2--3 of the
   [shallow-strip theorem](research_mixed_next_own_three_shallow_upper_strip_reduction.md)
   compare the row, at this same \(q\), with \(L_0\) or the
   row at \(v=3/10\). For \(q\le3/20\), its Section 4
   transports the joint first-main and next-row profile by
   \(dq=dv\) to \(q=3/20\) or \(v=3/10\). Its smallest
   displayed multiplier is \(3465/3328>1\). These calculations
   use (16), the negative height \(h_s\), and \(R\ge7/10\),
   but not \(x\). Both stopping profiles have just been paid
   with the same cap reserve. This proves (15) also here.

Clipping the first index at the current \(q\) only increases its
value. Its outside next rate stays fixed during clipping. This
completes the proof of (15) for all of (14), including both physical
endpoints. The extension used pointwise rates throughout, not the
central theorem's bound on a coherent product.

## 4. The complete horizontal finite source

The next lower physical block increases to its real low cut
\(3/20\). Its remaining below-half source uses the exact
canonical interpolation in
[complete currents](research_mixed_next_lower_left_complete_currents.md),
with heights \(-1/5,+4\), both horizontal Fourier remainders,
all four weighted half-sides and both unweighted joins. Each
comparison holds at the current \(q\), with an outside first
profile attached, and allows either sign of \(h_t\). Thus its
controlling rates belong to (14). Every next upper row is instead
bounded positively by its actual rate \(E_0(j/N)\), also in (14).
The zero-safe endpoint-uniform numerator and factorial estimates
have polynomial cost and arbitrarily small rate tolerance, including
\(j=D\). At that last index no uniform loss is borrowed from
the vanishing debit \(v/600\); (12) supplies the uniform loss.
Consequently
\[
 |C_{0,N}(Y,Z)|\le C_\tau N^{B_\tau}
             e^{N\{\max_{\varphi\in\mathscr P(y,z)}\varphi+\tau\}}.
 \tag{22}
\]
This is a direct complete-source upper estimate, not a new relative
packet or an assertion about a nonzero full-kernel coefficient.

For the first factor the exact groups are
\[
          0\le i<L_N,\qquad L_N\le i<M_N,\qquad M_N\le i<N.
 \tag{23}
\]
All first estimates in
[right horizontal, Sections 5--8](research_mixed_next_lower_left_incoming_right_horizontal.md)
are independent of the next own type and allow \(|Y|\le1\).
We specify the unchanged inventory and estimates so that their
use does not import an old next-kernel comparison.

The positive upper first rates are at most the maximum of their
real-half and last rates. For reflected index \(v\le11/50\),
their difference from last is at most
\(2\{J(v)-J(v/2)\}\le0\). For \(11/50\le v\le1/2\),
their difference from half is at most
\[
             \frac{29}{20}(1/2-v)+3J(v)\le0,                 \tag{24}
\]
whose endpoint at \(11/50\) is bounded by \(-479/11000\)
and whose other endpoint is zero. The upper-envelope convexity
proves the assertion. The positive finite version retains every
\(i\ge M_N\), including the even half row and the last index.
The first real half is at most its negative-height half profile:
on \(s=1/2+i\sigma\), \(h_s\le\sigma\le0\),
\(\Im Q_{1,s}\ge\pi(x-q)>0\). It can then be clipped and
paid by (15). The last alternative uses (10) and (8).

The first middle canonical row is
\[
 T_N(s;a,y)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                         E_N(a)E_N(y)E_N(s)^3.                \tag{25}
\]
Its half-grid boundaries are \((L_N-1/2)/N,(M_N-1/2)/N\).
The original argument bounds on \(c\le\Re s\le1/2\) give
\[
             -9\pi/5\le\Im Q_{1,s}\le19\pi/10.              \tag{26}
\]
The lower and upper aliases at \(-1/5,+4\) are consequently
below their same-index main profiles by \(\pi/50\) and
\(1541\pi/2500\), respectively. The four weighted vertical
rates decrease away from their real cuts with reserves
\(\pi/5,\pi/10\). The incoming boundary at \(x=s_R=1/2\)
uses the original continuous two-branch canonical upper rate;
both numerator-period terms remain, and no nonzero symbol at a
numerator zero is asserted.

Both unweighted sides remain. At \(c\), the incoming real
cotangent is nonpositive. On the negative-height side the positive
outgoing cotangent is less than \(4/3\) times the own one:
the exact maximum-ratio proof uses
\(\cosh(2\pi\sigma)<5/4\), \(\cos(2\pi c)>19/20\),
\(\sin(2\pi c)>3/10\), giving \(4/3\) in its nonmonotone
case. Thus the real phase is convex vertically. At the half cut,
the own real cotangent is zero and the shifted ones are nonpositive;
weak convexity suffices. Each side is bounded by its real/main
endpoints. The real low endpoint uses (10),(8); the main and half
endpoints use (15),(22).

The cotangent identity contains \(+N\) times the real middle
integral, both horizontal remainders and four weighted half-sides.
Moving only its constant mode adds exactly the two unweighted
sides just described. No residue or integer frequency is deleted.
At \(q=0\), the canonical factor \(E_N(y)\) uses the exact
[inward-seam continuation](research_factorial_symbol_across_inward_seam.md).
Separately the full forced polynomial satisfies
\[
 |d_N(Y)|\le C_\tau N^{B_\tau}
                         e^{N\{-\Re g(y)+\tau\}}.           \tag{27}
\]
These are distinct source statements; no relative asymptotic for
\(d_N\) is used. The \(O(1/N)\) half-grid changes are absorbed
by the original uniform integrated-rate continuity, including
numerator zeros. Finite sums and the original sampling factors
cost powers of \(N\). Choose their total rate tolerances inside
half of (12). Equations (8),(15),(22)--(27) prove the first line
of (6), with its weaker common deficit \(10^{-11}\).

## 5. First-kernel deformation on the corner rectangle

On \(a=x-i\eta\), \(1/2\le x\le7/10\),
\(0\le\eta\le9/125\), use only the first-kernel part of
[corner Gaussian deformation](research_mixed_next_lower_left_corner_gaussian_deformation.md).
It depends on \(a,y\), not on the following own type. The
[annulus](research_mixed_conditional_corner_root_annulus.md),
[angle guard](research_mixed_conditional_corner_root_angle.md),
and [prewall curvature](research_mixed_next_lower_left_corner_prewall_curvature.md)
give the original simple zero-lift point \(s_c(a,y)\), including
\(q=0\), with
\[
 Q_{1,s}(s_c;a,y)=0,\qquad
 2/25<\Re s_c<1-x,\qquad
 |\Im s_c|<\frac{\log2}{2\pi}.
 \tag{28}
\]
Set \(\Theta(a,y)=Q_1(s_c;a,y)\), \(M=\Re\Theta\).
On fixed local charts its actual local integral obeys
\[
 G_N(a,y)=N^{-1}\mathcal B(a,y)e^{N\Theta(a,y)}
                 (1+O_{\rm hol}(N^{-1})),\qquad\mathcal B\ne0.
 \tag{29}
\]
The coefficient and increasing-index orientation are the original
ones; its power is \(N\cdot N^{-3/2}\cdot N^{-1/2}=N^{-1}\).

We require the following source-level extraction, before any next
kernel is attached. For every prescribed \(\tau>0\),
\[
\begin{split}
 |U_{0,N}(w,X)\{C_{1,N}(X,Y)-G_N(a,y)\}|
 \le{}&C_\tau N^{B_\tau}|U_{0,N}(w,X)|e^{N(M-\gamma)}\\
      &+C_\tau N^{B_\tau}e^{N(B_0+\tau)},
\end{split}                                                     \tag{30}
\]
with a uniform \(\gamma>0\). This is the same un-attached
extraction proved in Section 2 of the
[deeper-radius corner](research_mixed_next_three_deep_radius_incoming_corner.md);
none of its proof of (30) uses \(R\le7/10\).

In detail, the first cuts here are
\(L_N=\lfloor2N/25\rfloor+1\), \(M_N=\lceil N/2\rceil\),
with half-grid cuts \(\ell_N,b_N\). The exact middle reduction
retains all lower and upper physical rows, aliases at \(-2,+2\),
and all four weighted sides. With the complete cap, their rates
are at most \(B_0\), \(32563/21000<B_0\), and \(13/10<B_0\).
Those original positive source estimates are uniform on \(|Y|\le1\).
The retained real integral moves to the height in (28), with both
unweighted sides. The prewall curvature and the exact postwall force
polynomials give a unique maximum \(M\), and a uniform strict loss
away from the regular critical chart. Those postwall proofs use
only \(|Y|\le1\), for either sign of the private height.

At the lower side, vertical convexity bounds the rate by the larger
real/main endpoint. At the half side the full two-branch rate
decreases up to height \(\eta\), then increases; its maximum
between zero and the critical height is again at an endpoint.
The two main endpoints have rate at most \(M-\gamma\); the
real endpoints, with the complete cap, have rate at most \(B_0\).
Uniform integrated-rate continuity covers the half-grid shifts at
both parities. The original canonical numerator is holomorphic
through its wall, and no denominator is introduced there. At
\(q=0\), the inward-seam factorial theorem supplies the same
local symbol in (29). These facts prove precisely the two terms
of (30), without importing the former next-type-four attachment.

## 6. Correlated action calibration and transport on the corner

Let \(B_*=B_U(1/2)\). At \(a=a_L\), (15) applies to
every \(2/25\le s_R\le1/2\) and every rate in (14), with
deficit greater than \(10^{-9}\). Let \(\widehat R\) be the
original continuous first-row upper rate and define
\[
 m(\sigma)=\max_{2/25\le v\le1/2}
                     \widehat R(v,\sigma;a_L,y).
 \tag{31}
\]
At this incoming half face, the prewall curvature theorem makes
\(m\) convex on \(|\sigma|\le\log2/(2\pi)\), with its
minimum at \(\Im s_c(a_L,y)\). The original first height
\(h_s\) also belongs to this interval. The continuous boundary
extension at \(v=1/2\) preserves this maximum comparison. Hence
\[
             \Re\Theta(a_L,y)\le m(h_s).                    \tag{32}
\]
Every next rate in (14) is held fixed during this first maximum.
Equations (15),(31)--(32) give
\[
 B_*+\Re\Theta(a_L,y)+\varphi-\Re g(y)
                <\Lambda_{123}(z)-10^{-9}
                    \quad(\varphi\in\mathscr P(y,z)).        \tag{33}
\]
The full physical upper-rate family is essential here; a bound on
the central coherent product alone would not imply (33).

On the bottom side of \(\widetilde\Gamma_C\), the complete
cap-only transport in
[selected corner, equation (18)](research_mixed_next_selected_incoming_corner_union.md)
has rate at most \(B_*+\tau\). On its right side, the
[seven-tenths cap theorem](research_mixed_cap_seven_tenths_vertical_bound.md)
gives \(3907/4500<7/8<B_*\), using the original
[cap-plane floor](research_mixed_next_calibrated_cap_plane_floor.md).
These are complete all-real-color cap bounds, independent of the
following own type. Thus on both sides
\[
           |U_{0,N}(w,X)|\le C_\tau N^{B_\tau}e^{N(B_*+\tau)}.
 \tag{34}
\]
For \(q>0\), the
[algebraic transport theorem](research_mixed_four_conditional_algebraic_transport_domain.md)
gives \(\Re\Theta_a<0\), \(\Im\Theta_a>0\) throughout the
incoming rectangle. Its hypotheses concern only \(a,y\).
The same derivative continues to \(q=0\) by the closed-seam
root theorem, so the weak limiting signs suffice there. Moving
rightward, then upward, therefore gives
\[
             \Re\Theta(a,y)\le\Re\Theta(a_L,y),
                        \qquad a\in\widetilde\Gamma_C.       \tag{35}
\]
Combining (22),(27),(33)--(35), with their total tolerance below
half of the reserve in (33), proves
\[
 |U_{0,N}(w,X)d_N(Y)C_{0,N}(Y,Z)|e^{N\Re\Theta(a,y)}
       \le CN^B e^{N\{\Lambda_{123}(z)-\tfrac12\,10^{-9}\}}.
 \tag{36}
\]

The first error in (30) is paid by (36), with its additional
\(e^{-N\gamma}\). The local term (29) is paid directly by
(36). For the second, raw upper-envelope term in (30), apply the
actual attachment theorem to \(V_N=e^{NB_0}\). This gives
\[
 |d_N(Y)C_{0,N}(Y,Z)|
 \le CN^B e^{N\{\Lambda_{123}(z)-B_0-1/200\}}.
\]
Multiplication by that envelope term, including its extra
\(\tau\), leaves deficit \(1/200-\tau\). Choose
\(\tau<1/1000\), so this deficit is greater than \(1/250\).
This uses absolute upper bounds, without identifying the envelope
as a separate source factor or dividing by a cap or Fourier weight
that might vanish.
Adding these finite terms proves the second line of (6).

For every fixed \(N,w,y,z\), the complete density (4) is entire
in \(a\): its \(a\)-dependent factors are finite Laurent
polynomials in \(e^{-2\pi ia}\), which never vanishes at finite
\(a\). Cauchy's theorem gives the exact oriented identity
\[
             N\int_{\Gamma_C}D_N(a)\,da
              =N\int_{\widetilde\Gamma_C}D_N(a)\,da.         \tag{37}
\]
Both side lengths are uniformly bounded. This proves the stated
combined old-corner estimate with the original positive \(N\).

## 7. Final real arc and the remaining obligations

The complete whole-disk source estimate in
[coherent far arc, equation (22)](research_mixed_next_coherent_cap_far_arc.md)
states
\[
 \sup_{\substack{7/10\le a\le1,\ |Y|\le1\\-2\le w\le2}}
 |U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)|
                         \le CN^B e^{153N/100}.              \tag{38}
\]
This is its complete finite cap-times-first theorem, prior to that
note's separate selected-sector application. Since \(153/100<B_0\),
it is an eligible preceding factor for (8) on the present lower
shared interval. This proves the third line of (6); no selected
\(Y^{-N}\) is borrowed from the old application.

Integrate (6) on \(\Gamma_H,\widetilde\Gamma_C,\Gamma_F\),
use (37), and retain the original outside factor \(+N\).
Their bounded lengths and finite additions change only the polynomial
prefactor, proving (7). This completes the first right path on the
actual family (1)--(3). The initial, tapered and central first paths
must still be assembled with their own eligible source theorems.
The old cardinal filter, the other shared-variable intervals and
both Fourier observations remain unchanged. In particular (7)
does not bound the remaining signed shared-variable contours or
establish a complete next-transfer asymptotic.
