# A fixed-cutoff holomorphic representative of the complete conditional source

Research deduction, 7 November 2026. A finite reciprocal-factorial
sum with a fixed upper index gives a joint holomorphic packet near
each real incoming reference. Subtracting the exact second period
produces an interpolant of the original conditional polynomial at
every incoming node in that neighborhood, for every free output.
The proof retains both entire endpoint currents, the two original
alias limits, and all contour joins.

The interpolant is not identified with the original conditional
polynomial off the incoming grid. Its incoming derivatives are not
substituted for ordinary boundary normals. No numerical evaluation
or new source certificate is used.

## 1. Fixed finite source and exact node values

Use the original conventions
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 X=e^{-2\pi ia},\quad W=e^{-2\pi iy},\qquad
 A=[267/1000,433/1000].
 \tag{1}
\]
Let \(E_N=1/\Pi_N\) be the original global reciprocal factorial.
It is holomorphic on \(\Re z<1\), and
\[
                         E_N(-j/N)=0\qquad(j\ge1).
 \tag{2}
\]
These are the exact zeros from
[the global factorial chart](research_mixed_fourier_right_cap_joint_global_chart.md);
no division by a vanishing recurrence factor is involved.

Fix \(a_0\in A\) and \(y_0=x_0=\xi_0+i\upsilon_0\). Choose a
sufficiently small fixed \(\epsilon>0\), and put
\[
 R=a_0+\epsilon<\frac12,\quad M_N=\lfloor NR\rfloor,\quad
 \alpha_N=-\frac1{2N},\quad
 \beta_N=\frac{M_N+1/2}{N}.
 \tag{3}
\]
In particular \(|\beta_N-R|\le1/(2N)\). Define
\[
\begin{split}
 \mathscr T_N(t;a,y)
   &=
 N e^{\pi iNa-\pi iN[(a-t)^2+t^2]-\pi ia}
                  E_N(a-t)E_N(t)^2E_N(y-t),\\
 J_{N,R}(a,y)&=\sum_{k=0}^{M_N}\mathscr T_N(k/N;a,y).
\end{split}
 \tag{4}
\]
The index \(M_N\) is independent of \(a,y\). Thus (4) is
holomorphic on a fixed complex neighborhood of \((a_0,y_0)\).
All the reciprocal arguments have real part less than one there.

At every physical \(a=b/N\), \(0\le b\le M_N\), the summands
with \(k>b\) vanish by (2), while the summands with \(k\le b\)
are exactly those of
[the initialized-source identity](research_mixed_three_left_cycle_initialized_source.md),
equation (6). Consequently
\[
                         J_{N,R}(b/N,y)=J_N(b/N,y).
 \tag{5}
\]
This equality holds for all \(y\) in the fixed-level strip
\(S_N=\{-1/(2N)<\Re y<1\}\), not just at output nodes.
In particular it holds for every physical incoming node satisfying
\(|b/N-a_0|\le\epsilon/4\).

Retain the exact second period \(\mathcal I_{2,N}\), and define
\[
 \widetilde C_{N,R}(a,y)
     =J_{N,R}(a,y)-N(W^N-1)\mathcal I_{2,N}(a,y).
 \tag{6}
\]
The initialized-source theorem gives the exact node identity
\[
 \boxed{\quad
 \widetilde C_{N,R}(b/N,y)=C_{0,N}(r^b,e^{-2\pi iy})
                \qquad(0\le b\le M_N,\ y\in S_N).
 \quad}
 \tag{7}
\]
Here \(\mathcal I_{2,N}\) uses its same-current fixed-level
extension to \(S_N^2\). All outgoing derivatives in (7) also
agree. The finite zeros in (2), rather than an off-grid support
restriction, prove (5)--(7).

## 2. Joint packet to be proved

Let \(\Phi_1(a,y)\), \(t_*(a,y)=-z_2(a,y)\), and
\[
 \mathcal F(t;a,y)
   =-g(a-t)-2g(t)-g(y-t)
                  +\pi i\{a-(a-t)^2-t^2\}
 \tag{8}
\]
have their original regular critical branches. The absolute
calibration is
\(\mathcal F(t_*;a,y)=\Phi_1(a,y)\), as in
[the left-contour calculation](research_mixed_three_left_cycle_left_contour.md).
At the center,
\[
 0<\Re t_*<\xi_0<a_0,\qquad
 0<h_0:=\Im t_*(a_0,y_0)<\upsilon_0.
 \tag{9}
\]
The critical point is nondegenerate and continues holomorphically.
Put
\[
 \mathcal C_J(a,y)=
 \frac{\sqrt{2\pi}\,e^{-\pi ia}}
 {\mathfrak a(a-t_*)\mathfrak a(t_*)^2
  \mathfrak a(y-t_*)\sqrt{-\mathcal F_{tt}(t_*;a,y)}} .
 \tag{10}
\]
The factorial symbols and the square-root branch are exactly
those in
[the complete physical-row packet](research_mixed_three_physical_input_complete_packet.md).
At the center the square root has positive real part; continue
it holomorphically on the small bidisk used below.

**Theorem 1.** For every \(a_0\in A\), one can choose
\(\epsilon>0\) in (3) and a fixed complex bidisk \(U\) about
\((a_0,y_0)\) such that, uniformly on smaller fixed bidisks,
both level parities satisfy
\[
\begin{split}
 J_{N,R}(a,y)
     &=N^{-1/2}\mathcal C_J(a,y)e^{N\Phi_1(a,y)}
                                      (1+O(N^{-1})),\\
 \widetilde C_{N,R}(a,y)
     &=N^{-1/2}\mathcal C_J(a,y)e^{N\Phi_1(a,y)}
                                      (1+O(N^{-1})).
\end{split}
 \tag{11}
\]
The coefficient in (10) is holomorphic and nonzero on \(U\).
Every fixed mixed \(a,y\) derivative of each normalized error
in (11) is \(O(N^{-1})\) on smaller bidisks. In particular both
chosen finite-source representatives are nonzero there for
sufficiently large \(N\).

The following proof establishes the required global persistence.
It does not infer a joint packet from the physical-row values
alone.

## 3. Exact contour identity for the fixed cutoff

For parameters near the center, (4) is holomorphic throughout
the strip \(\alpha_N\le\Re t\le\beta_N\), at all finite heights.
The exact cyclotomic-factorial end formulas give, at fixed \(N\),
\[
 \mathscr T_N(t;a,y)\sim
 \begin{cases}
 C_{+,N}(a,y)e^{2\pi i[N(a-1)+1]t},
                                  &\Im t\longrightarrow+\infty,\\
 C_{-,N}(a,y)e^{2\pi i[N(1-y)-1]t},
                                  &\Im t\longrightarrow-\infty .
 \end{cases}
 \tag{12}
\]
The constants are nonzero and are retained. These are the same
exact quadratic cancellations as in the left-contour theorem;
they do not require \(Na\) to be integral.

The upper and lower horizontal residue corrections therefore
decay with the respective positive rates
\[
                 2\pi(N\Re a+1),\qquad 2\pi(N\Re y+1).
 \tag{13}
\]
Both vanish at infinite height. With
\[
 w_{N,0}(v)=\frac1{1+e^{2\pi Nv}}-\mathbf1_{\{v<0\}},
 \tag{14}
\]
the original lattice residue formula gives exactly
\[
\begin{split}
 J_{N,R}={}&
 N\int_{\alpha_N+ih_0}^{\beta_N+ih_0}
                                    \mathscr T_N(t;a,y)\,dt\\
 &+iN\int_{\mathbb R}w_{N,0}(v)
       \{\mathscr T_N(\beta_N+iv;a,y)
                    -\mathscr T_N(\alpha_N+iv;a,y)\}\,dv\\
 &+iN\int_0^{h_0}
       \{\mathscr T_N(\alpha_N+iv;a,y)
                    -\mathscr T_N(\beta_N+iv;a,y)\}\,dv .
\end{split}
 \tag{15}
\]
Thus both whole endpoint currents and both unweighted joins
remain. Equation (13) justifies the fixed-level identity;
the uniform large-level bounds on its infinite currents are
proved separately below.

## 4. Bounded-height endpoint profiles, with both right factors retained

The left endpoint continues to have the exact midpoint factor
\[
                    |E_N(\alpha_N+iv)|^2
                              =\frac{1+e^{2\pi Nv}}N.
 \tag{16}
\]
On a fixed bounded height interval, its other two factorial
arguments are regular. Its continuous unweighted upper rate is
\[
\begin{split}
 L(v;a,y)={}&
 \Re\{\pi i[a-(a-iv)^2-(iv)^2]-g(a-iv)-g(y-iv)\}
                                      +2\pi v_+ .
\end{split}
 \tag{17}
\]
The corresponding weighted rate is \(L(v;a,y)-2\pi|v|\).
At the center, this is exactly the left rate \(\mathcal B_L\)
of the left-contour theorem. Its maximum is
\(\Re\Omega(a_0,y_0)<\Re\Phi_1(a_0,y_0)\), with a strict
gap supplied by the complete second-period action. The raw
left join on \(0\le v\le h_0\) also has a strict gap, by that
theorem's increasing-join and endpoint-concavity argument.
These profiles are continuous in \(a,y,v\). The midpoint
identity (16) treats \(v=0\) without a singular quotient.

At the new right endpoint one must reflect **both** reciprocal
factors, rather than keep the old incoming midpoint identity.
For all parameters, the exact identities are
\[
\begin{split}
 E_N(a-\beta_N-iv)
    &=(1+X^N e^{-2\pi Nv})E_N(1+a-\beta_N-iv),\\
 E_N(y-\beta_N-iv)
    &=(1+W^N e^{-2\pi Nv})E_N(1+y-\beta_N-iv).
\end{split}
 \tag{18}
\]
Both plus signs follow from \(e^{2\pi iN\beta_N}=-1\).
They give the zero-safe bounds
\[
\begin{split}
 |1+X^N e^{-2\pi Nv}|&\le2e^{2\pi N(\Im a-v)_+},\\
 |1+W^N e^{-2\pi Nv}|&\le2e^{2\pi N(\Im y-v)_+}.
\end{split}
 \tag{19}
\]
Neither moving zero line is divided out.

Choose the incoming bidisk small enough that
\(\Re a<a_0+\epsilon/4\). For large \(N\), the real parts of
\(1+a-\beta_N,\beta_N,1+y-\beta_N\) lie in compact
subintervals of \((0,1)\). The limiting right upper rate is
\[
\begin{split}
 Q_R(v;a,y)={}&
 \Re\{\pi i[a-(a-R-iv)^2-(R+iv)^2]\\
 &\hspace{9mm}-g(1+a-R-iv)-2g(R+iv)-g(1+y-R-iv)\}\\
 &+2\pi(\Im a-v)_++2\pi(\Im y-v)_+ .
\end{split}
 \tag{20}
\]
Every \(g\) in this formula is on its original regular strip.
For fixed \(\epsilon>0\), the ordinary regular packets and
(18)--(19) give, for \(|v|\le H\),
\[
 |\mathscr T_N(\beta_N+iv;a,y)|
                         \le C_{\epsilon,H}N^{-1}e^{NQ_R(v;a,y)}.
 \tag{21}
\]
The four reciprocal factors contribute \(N^{-2}\), and the
literal row contributes the outside \(N\). The \(O(N^{-1})\)
endpoint offset changes the exponent by \(O(1)\) on these
fixed regular strips. The constants may depend on the chosen
\(\epsilon\); it is fixed before \(N\) tends to infinity.

The passage back to the true endpoint is a passage of continuous
rates, not a uniform regular-symbol assertion at a factorial wall.
For real \(a=a_0\), as \(R\downarrow a_0\), (20) converges
uniformly on bounded \(v\)-intervals to
\[
\begin{split}
 \mathcal R(v)={}&2\pi a_0v-2\Re g(a_0+iv)
       -\Re g(1+y_0-a_0-iv)\\
       &+\pi(-v)_++2\pi(\upsilon_0-v)_+ .
\end{split}
 \tag{22}
\]
Indeed, the continuous original primitive at the remaining wall
satisfies
\[
                   -\Re g(1-iv)+2\pi(-v)_+=\pi(-v)_+ .
 \tag{23}
\]
For \(v>0\) the lower primitive has real part zero; for \(v<0\)
the upper reflection gives \(\Re g(1-iv)=\pi(-v)\).
Continuity at \(v=0\) completes (23).

The [whole right-contour theorem](research_mixed_three_left_cycle_right_contour.md)
proves
\[
\begin{split}
 \mathcal R(v)-2\pi|v|&\le E_R-\pi|v|/10,\\
 \mathcal R(v)&\le E_R-\pi v/50\qquad(0\le v\le h_0),\\
 E_R&<\Re\Phi_1(a_0,y_0)-1/20.
\end{split}
 \tag{24}
\]
Consequently, on any fixed bounded height interval, sufficiently
small \(\epsilon\) and then a sufficiently small parameter
bidisk preserve strict gaps for the weighted right profile
and the entire unweighted right join. Equations (18)--(23)
include both \(v=0\) and \(v=\upsilon_0\), and the nearby
moving lines \(v=\Im a,\Im y\).

## 5. Uniform control of the infinite ends

The choice of the bounded height cutoff can be made before the
small endpoint displacement. Start with a bounded parameter
neighborhood having \(\Re a,\Re y>0\), and with real endpoints
in a bounded neighborhood of \(0,a_0\). For sufficiently large
\(|v|\), every moving factorial argument is uniformly nonreal.
The global upper/lower cyclotomic formulas therefore apply
uniformly even as a real argument approaches its old endpoint
wall. This uses the
[original exact remainder bounds](research_exact_cyclotomic_factorial.md),
not a regular-strip symbol at that wall.

Beyond a fixed \(H>1+|\Im a|+|\Im y|\), the exact weighted
leading slopes are those in (13). A same-source comparison
between \(H\) and any larger height costs at most
\(8N\varepsilon_H\), where \(\varepsilon_H\to0\), after
counting the four reciprocal factors with multiplicity.
The finite geometric kernel factor is uniformly comparable to
its leading exponential there. The two period factors, if
(18) is used, also have their explicit nonzero leading factors
at these ends; their middle zeros never enter this comparison.

Choose one fixed \(H\) large enough that this remainder loss is
smaller than half the center endpoint loss at heights \(\pm H\).
The center losses grow linearly by (24) and by the left estimate
\(\mathcal B_L(v)\le\Re\Omega-2\pi\min(a_0,\xi_0)|v|\).
Now choose \(\epsilon\), and then the parameter bidisk, so that
the compact comparisons in Section 4 preserve those losses
at both \(H\) and \(-H\), as well as all bounded-height gaps.
Since \(\Re a,\Re y\) stay bounded below, the exact decay
rates (13) then integrate both entire tails uniformly.

It follows that there are fixed \(C,B,\delta>0\) such that
the sum of the absolute values of all four endpoint terms
in (15) is bounded by
\[
                  C N^B e^{N(\Re\Phi_1(a,y)-\delta)}
 \tag{25}
\]
on a fixed bidisk. The polynomial is harmless for the Gaussian
asymptotic. The order of choices is essential: a single tail
cutoff first, then the endpoint displacement and parameter
neighborhood, and finally sufficiently large \(N\).
Equation (25) controls the complete currents; fixed-level
vanishing in (12) alone would not have supplied it.

## 6. The moved saddle and its retained endpoint connectors

At the center, the entire raised segment \([0,a_0]+ih_0\)
has its unique maximum at \(t_0=t_*(a_0,y_0)\), by the
strict concavity and the subsequent strict decrease proved
in the right-contour theorem. Its endpoints have positive
gaps. Because the three factorial heights are
\(-h_0,h_0,\upsilon_0-h_0\), all separated from zero,
the original nonreal expansions apply throughout this segment.
They also apply to a sufficiently short extension from
\(a_0\) to \(R=a_0+\epsilon\). This extension and the two
half-grid offsets retain the endpoint gap.

For complex parameters near the center, retain first the fixed
center-height segment in (15). Put
\[
 \Delta t=t_*(a,y)-t_0,\quad
 L_N=\alpha_N+ih_0,\quad U_N=\beta_N+ih_0.
 \tag{26}
\]
Exact one-variable Cauchy deformation gives
\[
\begin{split}
 \int_{L_N}^{U_N}\mathscr T_N\,dt
   ={}&\int_{L_N+\Delta t}^{U_N+\Delta t}\mathscr T_N\,dt\\
     &+\int_{L_N}^{L_N+\Delta t}\mathscr T_N\,dt
       -\int_{U_N}^{U_N+\Delta t}\mathscr T_N\,dt.
\end{split}
 \tag{27}
\]
All intervening contours lie in the original holomorphic chart.
The last two connectors remain near the old raised endpoints,
and their compact strict gaps persist. They are included in
the error estimate, not discarded.

The translated segment in (27) passes through \(t_*(a,y)\)
at the same interior real coordinate as \(t_0\). Its local
horizontal Hessian remains accretive. On a fixed small
symmetric neighborhood of that point, the original regular
row packet is
\[
 \mathscr T_N
   =N^{-1}
     \frac{e^{-\pi ia}}
      {\mathfrak a(a-t)\mathfrak a(t)^2\mathfrak a(y-t)}
                 e^{N\mathcal F(t;a,y)}(1+O(N^{-1})).
 \tag{28}
\]
All other portions of the translated segment keep a uniform
positive loss relative to \(\Re\Phi_1(a,y)\). The lattice
density \(N\), the power in (28), and the one-dimensional
Gaussian give exactly (10)--(11). After \(N^{-1/2}\) rescaling,
the odd cubic and linear terms integrate to zero on the
symmetric local interval. Uniform quartic and symbol bounds
give the relative \(O(N^{-1})\) remainder.

Thus the moving critical point has actually been placed on
the integration contour. A local stationary expansion about
a point off the old fixed contour is not being assumed.

## 7. Exact subtraction, joint jets, and the finite observation

The [real-input action-gap theorem](research_mixed_three_real_input_action_gap.md)
already holds on a small complex neighborhood of this real
family and retains the complete periodic multiplier:
\[
 |N(W^N-1)\mathcal I_{2,N}(a,y)|
       \le C N^{-1/2}e^{N(\Re\Phi_1(a,y)-1/25)}.
 \tag{29}
\]
Shrinking the bidisk to its intersection with that neighborhood
proves the second line of (11). Both finite sums and the
same-current period are holomorphic, and (10) is nonzero.
Apply Cauchy's inequalities on nested bidisks to their normalized
errors to obtain every fixed mixed derivative claimed in
Theorem 1.

For completeness the corresponding chosen representative of
the entire twice-crossed Fourier source is
\[
\begin{split}
 \widetilde G_{-2,N,R}(a,y)
    &=\frac{\kappa^{-2}e^{\pi i(N-1)y}}N\,
                                      \widetilde C_{N,R}(a,y)\\
    &=\kappa^{-2}N^{-3/2}e^{-\pi iy}\mathcal C_J(a,y)
        e^{N\{\Phi_1(a,y)+\pi iy\}}(1+O(N^{-1})).
\end{split}
 \tag{30}
\]
At the incoming nodes in (7), this is the literal complete
\(\mathcal M_{-2}Z_N^{\rm cap}\), with all channels, scalars
and outgoing derivatives retained.

There is no assertion that \(\widetilde C_{N,R}=C_{0,N}\)
off the incoming grid. In particular the new mixed jets in
Theorem 1 are jets of the chosen interpolant. They do not
replace incoming ordinary normals of the original polynomial.
Different fixed cutoffs can give different off-grid functions
while agreeing at their common incoming nodes.

If \(\ell\) is an original prefix vector, and \(I_N\) is a
fixed set of incoming nodes lying in the local packet window,
the original power-two attachment, from
[the full-node composition theorem](research_mixed_three_homogeneous_period_full_node_composition.md),
Theorem 2, can use (7) in precisely the form
\[
 \ell^T A_2h(y)=e^{\pi i(N-1)y}
 \left\{
 \sum_{b\in I_N}\frac{(\ell^TS^{-1})_b}{P_b}
                   \widetilde C_{N,R}(b/N,y)
 +\sum_{b\notin I_N}\frac{(\ell^TS^{-1})_b}{P_b}
                   C_{0,N}(r^b,W)
 \right\}.
 \tag{31}
\]
The original node and ordinary-normal adapters are unchanged;
any normals already compiled into \(\ell\) remain there.
Neither the complementary sum nor its possible cancellation
is bounded by Theorem 1. A cardinal derivative row is generally
dense, and the original turn/interface operator need not
preserve \(I_N\). If (4) is used in a subsequent incoming
contour argument, all of that new contour's aliases and joins
must again be retained. The present result supplies a genuine
local holomorphic finite-source packet, not a whole incoming
period estimate or an arbitrary closing theorem.

## 8. Changing the cutoff changes only an exponentially smaller term

The finite sum in (4) depends on \(R\) away from incoming nodes.
The following estimate controls that dependence on a common
neighborhood. It allows two admissible nearby cutoffs to be compared
without appealing to uniqueness of interpolation.

**Proposition 2.** Fix \(a_0\in A\). There is an
\(\epsilon_*>0\) such that, for any two fixed cutoffs
\[
                  a_0<R_1<R_2<a_0+\epsilon_*,
 \tag{32}
\]
there are a fixed bidisk \(V\) about \((a_0,y_0)\) and constants
\(C,\delta>0\) for which
\[
\begin{split}
 |J_{N,R_2}(a,y)-J_{N,R_1}(a,y)|
       &\le C e^{N(\Re\Phi_1(a,y)-\delta)},\\
 |\widetilde C_{N,R_2}(a,y)-\widetilde C_{N,R_1}(a,y)|
       &\le C e^{N(\Re\Phi_1(a,y)-\delta)} .
\end{split}
 \tag{33}
\]
These bounds hold for both parities and all sufficiently large \(N\).
After multiplication by \(e^{-N\Phi_1}\), every fixed mixed
derivative of either difference satisfies the corresponding
exponentially small bound on smaller bidisks. Relative to the
leading term in (11), the differences and their normalized
derivatives are exponentially small as well.

*Proof.* Put \(M_{\nu,N}=\lfloor NR_\nu\rfloor\). Directly from
the finite definition,
\[
 J_{N,R_2}-J_{N,R_1}
       =\sum_{k=M_{1,N}+1}^{M_{2,N}}
                         \mathscr T_N(k/N;a,y).
 \tag{34}
\]
An empty sum is zero. Every index on the right satisfies
\(R_1<k/N\le R_2\). Choose \(V\) so that
\(\Re a<R_1\). For \(t\in[R_1,R_2]\), the real parts of
\(1+a-t,t,1+y-t\) then remain in compact subintervals of
\((0,1)\). At the sampled values \(t=k/N\), the two exact
reflection identities are
\[
\begin{split}
 E_N(a-t)&=(1-X^N)E_N(1+a-t),\\
 E_N(y-t)&=(1-W^N)E_N(1+y-t).
\end{split}
 \tag{35}
\]
The minus signs here differ from the half-grid signs in (18).
Their modulus bounds are
\[
 |1-X^N|\le2e^{2\pi N(\Im a)_+},\qquad
 |1-W^N|\le2e^{2\pi N(\Im y)_+}.
 \tag{36}
\]
Thus the regular factorial estimates give
\[
 |\mathscr T_N(k/N;a,y)|
                  \le C N^{-1}e^{NQ_{k/N}(0;a,y)},
 \tag{37}
\]
where \(Q_t\) is exactly the rate (20) with \(R=t\). The
constants may depend on the two fixed cutoffs.

At the center, \(Q_t(0;a_0,y_0)\) tends to \(E_R(a_0,y_0)\)
as \(t\downarrow a_0\), by (22)--(23). The endpoint gap in
(24) is greater than \(1/20\). First choose \(\epsilon_*\)
so that this gap stays positive for
\(a_0<t<a_0+\epsilon_*\). After fixing \(R_1,R_2\), continuity
on their compact interval and shrinking \(V\) yield
\[
 Q_t(0;a,y)\le \Re\Phi_1(a,y)-\delta
       \quad(t\in[R_1,R_2],\ (a,y)\in V)
 \tag{38}
\]
for one \(\delta>0\). Summing (37) over at most \(N\) rows
proves the first inequality in (33). The same second-period
term is subtracted for both cutoffs, so their corrected
difference is identical to (34).

Both differences are holomorphic on \(V\). Multiplication by
\(e^{-N\Phi_1}\) turns (33) into a uniform bound
\(Ce^{-N\delta}\). Cauchy's inequalities on nested bidisks
give its fixed mixed derivatives. Dividing further by the
nonzero coefficient \(\mathcal C_J\) and multiplying by
\(N^{1/2}\) gives the relative statement; this polynomial
factor can be absorbed by decreasing \(\delta\).
\(\square\)

This comparison concerns the nearby fixed-cutoff representatives.
It supplies no estimate for their difference from the original
polynomial at unsampled incoming arguments. It also does not
permit an exponentially small local error to be discarded
after an arbitrary subsequent crossing: that composition must
be estimated with its original weights.
