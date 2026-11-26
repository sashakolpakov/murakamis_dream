# The complete conditional source with a half cut below the incoming zero

Research deduction, 7 November 2026. A retained contour may cross the
incoming numerator wall without first estimating its physical wall rows
separately. The construction below retains every index below one half.
It proves the complete original conditional packet whenever its
nonnegative critical height lies strictly below the incoming depth.

The height condition is explicit; it is not established on the whole
displaced parameter rectangle here. In particular this note does not
replace a missing radius inequality by finite-level holomorphy. It uses
the proved lower-half-plane factorial asymptotic, and retains both
cyclotomic branches in every contour remainder. No numerical evaluation
or change to an earlier frozen note is used.

## 1. Exact source and statement

Keep
\[
\begin{gathered}
a=x-i\eta,\quad \tfrac12\le x\le\tfrac7{10},\quad
0\le\eta\le\tfrac9{125},\qquad
y=z+iH,\quad\tfrac{11}{50}\le z\le\tfrac9{20},\quad
0\le H\le\tfrac1{100},\\
X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad r=e^{-2\pi i/N},
\quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
C_{1,N}(X,Y)=\sum_{j=0}^{N-1}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
\end{gathered}                                                     \tag{1}
\]
The [negative-height branch theorem](research_mixed_conditional_negative_height_branch.md)
gives the original simple critical point \(s_*=u_*+ih_*\), zero
logarithmic lift and phase
\[
\begin{split}
Q(s;a,y)&=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias,\\
Q_s(s_*;a,y)&=0,\qquad \Theta(a,y)=Q(s_*;a,y),\\
\tfrac1{16}<u_*<1-x,\qquad
M(a,y):=\Re\Theta(a,y)&>\tfrac{13}{24}.
\end{split}                                                       \tag{2}
\]
The last floor and the exact original additive constant are supplied by
[height-action monotonicity](research_mixed_conditional_height_action_monotonicity.md).
The original \(g'\) is \(\Log(1-e^{-2\pi iq})\) on its regular strip.

**Theorem.** Let \(\mathcal K\) be a compact subset of (1) satisfying
\[
                              0\le h_*<\eta.                    \tag{3}
\]
On a fixed complex neighborhood of \(\mathcal K\),
\[
 C_{1,N}(X,Y)=N^{-1}\mathcal B(a,y)e^{N\Theta(a,y)}
                      (1+O_{\rm hol}(N^{-1})),\qquad
                              \mathcal B(a,y)\ne0.               \tag{4}
\]
The coefficient is the original one in (23) below. Both level parities,
all original physical rows and all fixed mixed derivatives are included.
No wall-action comparison \(M>\mathcal R(1-x)\) is assumed.

The earlier [wall-gap completion](research_mixed_conditional_wall_gap_completion.md)
already proves the packet when \(h_*\le0\). The distinct input in (4)
is a contour through the positive-height saddle that remains below the
incoming numerator's real zero line.

## 2. The factorial across the wall and the exact two-branch identity

Write \(\Pi_N(q)=P_N(Nq)\) for the original marked factorial and
\(E_N=1/\Pi_N\). The literal interpolant is
\[
 T_N(s)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                         E_N(a)E_N(y)E_N(s)^3.                  \tag{5}
\]
It agrees with the summand in (1) at \(s=j/N\).
The [global chart theorem](research_mixed_fourier_right_cap_joint_global_chart.md)
proves that (5) is holomorphic on the retained rectangles used below,
including \(\Re(a+s)=1\). More is needed for its asymptotic.

Theorem 1 of [the lower-half factorial continuation](research_lower_half_factorial_continuation.md)
gives the original nonzero symbol and holomorphic asymptotic on every
compact subset of \(\Im q<0\), with no real-part restriction. In
particular it applies to \(q=a+s\) on the whole main line in (3),
even after that line crosses \(\Re(a+s)=1\).
Its phase is the original lower-half continuation of \(g\), including
its constant. This is a proved asymptotic of the specified interpolation,
not an inference from entireness.

For the other currents the full period identity is retained:
\[
 \Pi_N(q+1)=(1-e^{-2\pi iNq})\Pi_N(q).                            \tag{6}
\]
Thus when \(\Re(a+s)\ge1\), put \(q=a+s-1\). The zero-safe upper
rate for the incoming factor is
\[
           \Re g(q)+\max\{0,2\pi\Im q\}.                        \tag{7}
\]
Both terms of \(1-e^{-2\pi iNq}\) are bounded, not discarded.
For \(0<\Re q<1\), (7) follows directly from the original regular
factorial expansion and (6). At \(\Re q=0\), it follows from the
midpoint bound in
[uniform factorial bounds, Lemma 1](research_uniform_factorial_and_boundary_decay.md),
applied with the \(1/(2N)\) shift, and the exact factor (6).
The integrated logarithm changes by \(O(\log N/N)\) under this shift.
Consequently the same upper rate, with polynomial factors or any fixed
small exponential allowance, holds uniformly through the endpoint and
all cyclotomic zeros. The upper/lower continuations in
[the half-plane theorem](research_factorial_uniform_halfplane_continuation.md)
fix the branches away from that line.

The same uniform bound from the prewall side includes points within
\(O(N^{-1})\) of \(\Re(a+s)=1\). Explicitly, retain the exact reflection
\[
 G_N(Nq)=\frac{N}{G_N(N(1-q)-1)}.
\]
Section 2, equation (4), of the same uniform-factorial note applies to its reciprocal
midpoint argument \(1-q-1/(2N)\), including both signs of its real
part and every reciprocal zero. It gives the continued original
prewall rate, with the same \(O(\log N)\) logarithmic error. Together
with (6)--(7), this supplies one uniform upper bound on both sides of
the wall, also for the even half-grid cut approaching it. No
nonvanishing symbol at the real positive cut is asserted.

For clarity, the incoming shifted chart itself is
\[
 \widetilde T_N(s)=e^{2\pi iNas}\Pi_N(a+s-1)\Pi_N(y+s)
                        E_N(a-1)E_N(y)E_N(s)^3.
\]
Its chirp is still \(a\), not \(a-1\). With \(A=e^{-2\pi iNa}\),
\[
 T_N(s)=\widetilde T_N(s)
               \frac{1-Ae^{-2\pi iNs}}{1-A},\qquad |A|<1.       \tag{8}
\]
The apparent extra poles of this chart are
\[
 s_k=1-a-k/N,\quad
 \operatorname{Res}_{s=s_k}\widetilde T_N(s)
 =\frac{e^{2\pi iNa s_k}P_{N-k}\Pi_N(y+s_k)
                  E_N(a-1)E_N(y)E_N(s_k)^3}{2\pi iN},
 \quad 1\le k<N.                                                \tag{9}
\]
They lie at height \(\eta>h_*\). Formula (8) cancels their residues
pointwise before any contour is moved. If the two terms are moved
separately, the explicit diagonal residues and the unpenalized shifted
current in
[the shifted-current identity, Sections 2--3](research_mixed_fourier_right_cap_shifted_current_identity.md)
must be retained, with \(q\) there replaced by \(a\) and the unchanged
chirp in (8). The proof below instead uses the holomorphic original
(5) throughout. It never drops those residue contributions by treating
\(\widetilde T_N\) as holomorphic.

## 3. A decreasing horizontal profile after the wall

For \(s=t+i\sigma\), \(1-x\le t\le1/2\), \(\sigma\ge0\), put
\[
 U=e^{2\pi\sigma}\ge1,\qquad T=e^{2\pi\eta}<8/5,\qquad
 R_y=e^{2\pi H}<8/7 .
\]
The two phase branches in (7) have the same real horizontal derivative:
their difference has derivative \(-2\pi i\). Its exact force modulus is
\[
 |e^{Q_s}|^2=
 \frac{|T-Ue^{-2\pi i(x+t)}|^2
       |1-R_yUe^{-2\pi i(z+t)}|^2}
      {|1-Ue^{-2\pi it}|^6}.                                   \tag{10}
\]
The factor \(T\) includes the original incoming chirp.
Since \(x+t\in[1,6/5]\) and \(t\in[3/10,1/2]\),
\[
 \cos 2\pi(x+t)>3/10,\qquad \cos2\pi t<-3/10.
\]
Consequently
\[
 |e^{Q_s}|^2
 \le
 \frac{(U^2-3U/5+64/25)(1+8U/7)^2}
      {(U^2+3U/5+1)^3}<1.                                    \tag{11}
\]
For the last inequality, denominator minus numerator is
\[
 U^6+\frac95U^5+\frac{3398}{1225}U^4
 +\frac{14173}{6125}U^3+\frac{1357}{1225}U^2
 -\frac{604}{175}U-\frac{39}{25}>0.
\]
For \(U\ge1\), retaining only
\(U^6+9U^5/5+2U^4+U^2-604U/175-39/25\)
bounds it below by \((411U-273)/175\ge138/175\).
This is a written polynomial inequality, not a root evaluation.

Before the wall the original phase is strictly horizontally concave.
It has its unique maximum at \(s_*\) on height \(h_*\).
After the wall (11) makes the continued real phase strictly decrease.
In (3) that main line is entirely below the incoming zero, so the
lower-half symbol is regular across the joining point. The whole main
line up to the half cut therefore has the same unique nondegenerate
maximum \(M\). Its right endpoint has a uniform strict gap on
\(\mathcal K\); this follows already from a fixed prewall segment
strictly to the right of \(u_*\), followed by monotonicity.

## 4. Every weighted side and horizontal alias

Let \(\widehat R(t,\sigma)\) be the upper rate of the original
interpolant (5): use the original \(\Re Q\) before the wall and
(7) after it. It is continuous across the wall and across the
cyclotomic line. At \(\sigma=0\) it is exactly the original continuous
physical rate \(\mathcal R(t)\).

The prewall derivative bounds are those in
[the full-depth lower-current theorem, Section 3](research_mixed_conditional_negative_height_lower_currents.md):
\[
 \partial_\sigma\widehat R\le9\pi/5\quad(\sigma\ge0),\qquad
 \partial_\sigma\widehat R\ge-33\pi/20\quad(\sigma\le0).
                                                                    \tag{12}
\]
Here all retained real indices are at least \(1/20\).

For the postwall part write \(r_0=x+t-1\in[0,1/5]\), and let
\(A(q)=\Arg(1-e^{-2\pi iq})\) on the original regular strip.
Away from the separating line, the exact derivative of (7) gives
\[
 \partial_\sigma\widehat R
 =-A(r_0+i(\sigma-\eta))-A(y+t+i\sigma)
   +3A(t+i\sigma)-2\pi x+2\pi{\bf1}_{\{\sigma>\eta\}}.           \tag{13}
\]
At \(r_0=0\) take the appropriate one-sided limits; the rate itself
is continuous. Notice that \(z+t>1/2\), so the outgoing argument
is nonpositive at every height.

For \(\sigma\ge0\) and \(\sigma\le\eta\), use
\(A(r_0+i(\sigma-\eta))\ge0\),
\(A(y+t+i\sigma)\ge\pi-2\pi(z+t)\), and
\(A(t+i\sigma)\le\pi-2\pi t\). Their substitution in (13)
gives an upper bound \(\pi(2+2z-4t-2x)\le3\pi/10\).
For \(\sigma\ge\eta\), instead
\(A(r_0+i(\sigma-\eta))\ge\pi/2-\pi r_0\), and the same
other bounds give
\[
 \partial_\sigma\widehat R
 \le\pi(5/2-x-3t+2z)\le9\pi/5.                               \tag{14}
\]
For \(\sigma\le0\), the incoming radius is at most one, so
\(A(r_0+i(\sigma-\eta))\le\pi/2-\pi r_0\).
The own and negative-outgoing terms are nonnegative. Hence
\[
              \partial_\sigma\widehat R\ge-19\pi/10.
                                                                    \tag{15}
\]
For \(\sigma\le-1/8\), the incoming radius is less than \(1/2\):
\(e^{-\pi/4}<1/2\) follows from \(\log2<7/10<\pi/4\).
The disk argument bound improves (15) to
\[
              \partial_\sigma\widehat R
                      \ge-\pi/6-7\pi/5=-47\pi/30.             \tag{16}
\]
These inequalities integrate through the finite boundary kink.
The two cyclotomic terms in (6) are responsible for the last term
of (13); omitting that term would give an incorrect upper alias.

Use the exact split cotangent rectangle at outer heights \(\pm2\).
On each half-grid side its remainder kernel has modulus at most
\(2e^{-2\pi N|\sigma|}\), and on the horizontal sides at most
\(4e^{-2\pi N|\sigma|}\). Equations (12)--(16) reduce every
weighted vertical side to its real cut value, with positive linear
loss. In particular, on postwall lower sides the loss is at least
\(\pi|\sigma|/10\), and on upper sides at least \(\pi\sigma/5\).

For the horizontal sides the original real rate satisfies, throughout
the entire interval \(0<t\le1/2\),
\[
               \mathcal R(t)<\tfrac74 t-3J(t)<11/8.            \tag{17}
\]
This uses the literal factor bounds, including the chirp, from the
lower-current theorem and does not require a prewall index.
At height \(+2\) the alias loss is at least \(2\pi/5\).
At height \(-2\) the prewall loss is \(7\pi/10\); on the
postwall part (15)--(16) give the larger loss
\(\pi/80+13\pi/16=33\pi/40\).
Thus both horizontal remainders have rate at most
\[
                 11/8-2\pi/5<7/40<M.                         \tag{18}
\]
All complete sides, not just their endpoints, have been retained.

## 5. The half-cut connector and the exact row inventory

Set
\[
 L_N=\lfloor N/16\rfloor+1,\quad M_N=\lceil N/2\rceil,\quad
 \ell_N=(L_N-1/2)/N,\quad b_N=(M_N-1/2)/N.                     \tag{19}
\]
The retained indices are exactly \(L_N\le j<M_N\).
The lower physical rows and the real lower cut are paid by the
lower-current theorem. Every physical row \(j\ge M_N\) is paid by
[the full upper-half theorem](research_mixed_conditional_negative_height_upper_half.md).
Its zero-safe physical rate and continuity also pay the real cut
\(b_N\), which differs from \(1/2\) by at most \(1/(2N)\).
In particular neither the odd case \(b_N=1/2\) nor any revived row
is removed by a false support rule.

At the exact limiting half cut \(s=1/2+i\sigma\), \(0\le\sigma\le h_*\),
condition (3) gives \(\sigma-\eta<0\). The own logarithmic argument
is zero. The continued incoming argument is nonnegative, and the
outgoing one is at least \(-2\pi z\). Thus, on the lower-half
continuation already justified in Section 2,
\[
 \Im Q_s(1/2+i\sigma;a,y)\ge2\pi(x-z)\ge\pi/10,
 \qquad
 \partial_\sigma\Re Q(1/2+i\sigma;a,y)\le-\pi/10.               \tag{20}
\]
The whole upper unweighted connector is therefore bounded by its
paid real endpoint. Compactness in (3) keeps its incoming numerator
a fixed distance below the real zero line. Ordinary continuity
preserves (20), with for example \(-\pi/20\), on the actual
half-grid cut \(b_N\) for all large \(N\).

The lower unweighted connector is already paid in the lower-current
theorem: it stays in the original prewall chart and uses vertical
convexity and its two paid endpoints. Section 4 pays the four
weighted vertical half-sides and both horizontal aliases. No
absolute estimate of the physical wall rows has entered this proof;
those rows are part of the retained original finite cycle.

The exact identity is
\[
 \begin{split}
 \sum_{j=L_N}^{M_N-1}T_N(j/N)
 &=N\int_{\ell_N}^{b_N}T_N(t)\,dt+\mathcal R_N,\\
 \mathcal R_N&=\frac{N}{2i}\left\{
 \int_{\partial R^+}T_N(s)[\cot(\pi Ns)+i]\,ds+
 \int_{\partial R^-}T_N(s)[\cot(\pi Ns)-i]\,ds\right\}.
 \end{split}                                                     \tag{21}
\]
Each sign-half boundary here omits the real segment and has its
original induced orientation. Holomorphy of (5) gives exactly
the same residues and the density \(+N\) after crossing the
positive numerator wall. The deformation of its real integral
to height \(h_*\) retains both unweighted connectors just paid.
There is no additional residue in this deformation of the original
chart; the artificial poles (9) belong only to the separated shifted
chart and have already been canceled in (8).

## 6. Gaussian coefficient, neighborhoods, and limitations

On the main line the actual factorial asymptotic gives
\[
 \begin{gathered}
 T_N(s)=N^{-3/2}b(s;a,y)e^{NQ(s;a,y)}
                                  (1+O_{\rm hol}(N^{-1})),\\
 b(s;a,y)=\frac{a_0(a+s)a_0(y+s)}
                      {a_0(s)^3a_0(a)a_0(y)},\qquad
 a_0(q)=\sqrt{2\sin\pi q}\,e^{-i\pi q/2}.                       \tag{22}
 \end{gathered}
\]
The incoming symbol across the wall is its actual lower-half
continuation; all other arguments retain their original symbols.
At the saddle every argument is in the original regular strip.
Consequently
\[
 \mathcal B(a,y)=
       \frac{\sqrt{2\pi}\,b(s_*;a,y)}
                        {\sqrt{-Q_{ss}(s_*;a,y)}}\ne0,          \tag{23}
\]
with the original accretive Gaussian branch. The row power,
cycle density and Gaussian width give
\(N^{-3/2}N N^{-1/2}=N^{-1}\).
Horizontal uniqueness from Section 3 and all paid groups above
give (4), including its original action and nonzero coefficient.

At each base point fix the integer row sets, alias rectangle, main
height and connectors before varying parameters. The strict gap
\(\eta-h_*>0\), regular main symbol, simple saddle and all source
reserves persist on a fixed neighborhood. The zero-safe upper
bounds in Sections 2 and 4 apply also to neighborhoods of the
cyclotomic line on the alias paths. A finite cover of \(\mathcal K\)
makes the remainder bounds uniform. The exact finite function and
the original phase agree on overlaps, and Cauchy's formula gives
all fixed normalized mixed derivatives on smaller neighborhoods.

This proves a complete conditional-source theorem under (3),
rather than a local phase theorem. Establishing (3) for all positive
critical heights on a desired actual parameter face is a separate
algebraic task. No cap estimate, selected affine comparison, whole
next-transfer asymptotic, or new knot-family conclusion is asserted.

