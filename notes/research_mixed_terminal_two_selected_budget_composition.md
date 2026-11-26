# Composing two selected lifts without spending shared curvature twice

Research deduction, 6 November 2026. The completed one-selected terminal
certificates can be reused after lifting the preceding retained
coordinate. Their common ordinary-index force has the opposite sign
to the force from this new lift. Convexity of the scalar conjugate
therefore combines the two budgets using the same full index cost.

For each fixed pair \((\gamma,\epsilon)\), this reduces all
108 terminal-label comparisons in the
[two-selected window](research_mixed_terminal_two_selected_window.md)
to two ordinary-lift inequalities on the actual reference family.
There are 216 comparisons across the two terminal types for a fixed
\(\gamma\); the same two functions are used on the union of all
four \((\gamma,\epsilon)\) reference families.
Those two inequalities are not proved here. The reduction does not
apply the completed terminal theorem at a height outside its stated
domain, and it introduces no new reference equation, numerical gain
or source evaluation.

## 1. Original reference and the two separate lift data

Use the original suffix
\[
       (3+\gamma,4,4,3+\epsilon),\qquad m\ge4,
\tag{1}
\]
and the notation \(c,r,b,s,a,t,v\) of the two-selected window.
The incoming coordinate \(c\) is unselected. Both \(b,a\) are selected
at \(H=1/100\). Their actual reference heights are negative.
The [backward reconstruction](research_mixed_terminal_two_selected_reference_reconstruction.md)
identifies every such reference with the already constructed terminal
family \(q_\epsilon(b)\), followed by the original rational transfers
for \(r,c\), on the filtered domain \(\Omega^K_{\gamma,\epsilon}\).
In particular
\[
 r,b,s,a\in O_4,\qquad
 .24<\Re(r,b,s,a)<.36,\qquad
 -.102<\Im(r,b,s,a)<-.001 .
\tag{2}
\]
Stars on these reference coordinates are suppressed below.
All logarithms and phase constants retain their original lifts.

Write
\[
\begin{split}
 Q(r;c,b)&=g(r+c)+g(r+b)-3g(r)-g(c)-g(b)+2\pi icr,\\
 Q(s;b,a)&=g(s+b)+g(s+a)-3g(s)-g(b)-g(a)+2\pi ibs,\\
 F&=Q(r;c,b)+Q(s;b,a)+\Phi_\epsilon(a;t,v)
                         -g(b)-g(a)-\frac{\gamma}{2}g(c).
\end{split}
\tag{3}
\]
Its internal derivatives vanish at the original reference. The only
remaining marginal is the full complex \(p_c=F_c\), which is
subtracted in every comparison.

Put
\[
 \Delta_b=H-\Im b,\quad \Delta_a=H-\Im a,\quad
 \bar b=b+i\Delta_b,\quad \bar a=a+i\Delta_a,
\tag{4}
\]
and define the exact differences
\[
\begin{split}
 B(z;d)&=g(z+id)-g(z)-idg'(z),\\
 L(z;d)&=g'(z+id)-g'(z).
\end{split}
\tag{5}
\]
For \(\mu=1,0\), respectively the factorial and forced alternative
of the complete selected weight at \(b\), set
\[
\begin{split}
 V_b={}&\Re\{B(r+b;\Delta_b)+B(s+b;\Delta_b)-3B(b;\Delta_b)\},\\
 T_{b,\mu}={}&V_b+(1-\mu)\Re g(\bar b)-2\pi\mu H,\\
 A_r={}&\Re L(r+b;\Delta_b),\\
 A_{b,\mu}={}&\Re\{L(r+b;\Delta_b)+L(s+b;\Delta_b)
                                      -3L(b;\Delta_b)\}
                                 +(1-\mu)\Re g'(\bar b),\\
 u={}&\Re L(s+b;\Delta_b)-2\pi\Delta_b .
\end{split}
\tag{6}
\]
The contribution from the \(a\)-lift to the same ordinary index is
\[
                         v_s=\Re L(s+a;\Delta_a).
\tag{7}
\]
Thus the actual shared force after both lifts is \(u+v_s\), not
two independent forces. The original \(b\)-stationarity equation
\[
             g'(r+b)+g'(s+b)-3g'(b)+2\pi is=0
\tag{8}
\]
is needed in (6). Replacing the reference by an arbitrary point
of its enclosing rectangle would leave additional residual terms.

There is no \(b,a\) mixed derivative in (3): their only shared
variable is \(s\). Consequently the lifted trial value is the sum
of the two one-coordinate trial values, and the only shared
horizontal force is (6)--(7). This exact additivity also holds when
the terminal part is replaced by a valid upper function depending
on \(a\) and its terminal targets.

## 2. Opposite forces and an exact convexity inequality

For a convex function \(\varphi\) on a real interval \(I\), with
reference center \(x_*\in I\), define
\[
 G_{\varphi,I}(q)=
       \sup_{x\in I}\{q(x-x_*)-\varphi(x)+\varphi(x_*)
                                      +\varphi'(x_*)(x-x_*)\}.
\tag{9}
\]
This function is convex in \(q\), is nonnegative, and has \(G(0)=0\).
Nonnegativity follows from the allowed target \(x=x_*\); the last
identity uses convexity of \(\varphi\).

**Lemma 1.** If \(u\le0\le v\), then
\[
                    G(u+v)\le\max\{G(u),G(v)\}
                                      \le G(u)+G(v).
\tag{10}
\]

*Proof.* The number \(u+v\) belongs to the interval \([u,v]\).
Convexity bounds its value by the larger endpoint value.
Both endpoint values are nonnegative. \(\square\)

No quadratic approximation is used in (10). In particular it
does not replace the one available curvature cost by two costs.
It compares its single conjugate at the summed force with the
sum of two conjugates of that same cost.

**Lemma 2.** On every actual reference in (2),
\[
                               u<0<v_s.
\tag{11}
\]

*Proof.* The real parts of \(s+b\) and \(s+a\) lie in
\((.48,.72)\subset(1/4,3/4)\). For \(z=x+iy\) in this
vertical strip,
\[
 \Im\cot(\pi z)=
       -\frac{\sinh(2\pi y)}{\cosh(2\pi y)-\cos(2\pi x)},
       \qquad |\Im\cot(\pi z)|<1 .
\tag{12}
\]
Indeed the cosine is strictly negative and
\(|\sinh(2\pi y)|<\cosh(2\pi y)\).
The whole two vertical segments in (5) stay in this strip.
Since \(g''=\pi\cot(\pi z)-i\pi\),
\[
\begin{split}
 u&=-\pi\Delta_b\int_0^1
           \{1+\Im\cot\pi(s+b+i\theta\Delta_b)\}\,d\theta<0,\\
 v_s&=\pi\Delta_a\int_0^1
           \{1-\Im\cot\pi(s+a+i\theta\Delta_a)\}\,d\theta>0 .
\end{split}
\tag{13}
\]
Both \(\Delta_b,\Delta_a\) are positive. The first chirp in
(13) is the \(-2\pi\Delta_b\) term of (6), and cannot be
discarded. \(\square\)

## 3. The two added ordinary budgets

For the original real-height function \(g_h(x)=\Re g(x+ih)\),
use (9) with the following costs and targets:
\[
\begin{array}{c|c|c}
 \text{node}&\varphi(x)&I\\ \hline
 r&2g_{\Im r}(x)&[.22,.5]\\
 b&(\mu+1)g_H(x)&I_\mu\\
 s&2g_{\Im s}(x)&[.22,.5].
\end{array}
\tag{14}
\]
The centers are \(\Re r,\Re b,\Re s\), respectively.
Take \(I_1=P=[.22,.45]\). Either \(I_0=P\) or the proved
forced-dominance interval \(I_0=[.4,.45]\) may be used.
For \(b\) in the latter case keep the signed conjugate; its
center need not belong to its target interval. Lemma 1 is used
only for the \(s\) cost, whose center does belong to its interval.
Write the three conjugates as \(G_r,G_{b,\mu},G_s\), and set
\[
 \boxed{\quad
 \mathfrak B_\mu
      =T_{b,\mu}+G_r(A_r)+G_{b,\mu}(A_{b,\mu})+G_s(u).
 \quad}
\tag{15}
\]
These are two scalar functions on the filtered reference family,
not 108 terminal-profile functions. They are the natural
one-selected ordinary-main increment budgets. Their definition
alone does not assert a complete ordinary finite-source theorem.

The [symmetric pair theorem](research_mixed_terminal_symmetric_pair_costs.md)
and the two-selected window give the simultaneous costs
\[
       2g_r,\quad(\mu+1)g_H,\quad2g_s
\tag{16}
\]
in the actual two-lift target Hessian. The remaining terminal-node
costs are exactly those of the one-selected certificate being
used. This is not an addition of two Hessian inequalities which
would count \(2g_s\) twice.

For an entirely algebraic upper bound in (15), the cubic
coefficients can be taken to be
\[
             \frac{88}{5},\qquad
             (\mu+1)\frac{49}{5},\qquad
             \frac{88}{5}.
\tag{17}
\]
They follow from the original height bounds (2) and the
[cubic-cost theorem](research_mixed_terminal_cubic_cost_and_response_bounds.md).
The [signed uncertain-center formula](research_signed_cubic_gain_with_uncertain_center.md)
retains a negative \(b\)-gain on a disjoint forced interval.
Its force convexity also permits shared-force endpoint bounds
after actual force and center enclosures have been justified.
No such new enclosures or gains are evaluated here.

## 4. All completed terminal certificate routes compose

Fix a terminal label \(\sigma\), alternative \(\nu\) at \(a\),
and one of its already proved certificate routes. Before outward
rounding its scalar upper has the form
\[
                \mathfrak A_{\sigma,\nu}
                         =T_{\sigma,\nu}+G_s(v_s)
                                             +R_{\sigma,\nu},
\tag{18}
\]
where \(R_{\sigma,\nu}\) contains only the terminal-node gains
and any original bare-source upper. The same \(s\) cost in
(14) can be retained in every route.

This follows directly from the actual completed proofs:

* For main and private-left profiles, \(R_{\sigma,\nu}\) contains
  the selected \(a\) and terminal \(t\) costs, with the proved
  private-left force change and optimizer domain where applicable.
* For a real transform cut or entropy profile, the
  [direct-cut reduction](research_mixed_terminal_real_transform_cut_budget.md)
  eliminates the private target at the original reference.
  Its remaining selected cost and bare upper enter \(R\).
* For the alias, constant and remaining face bounds, the
  [joined-plane theorem](research_mixed_terminal_uniform_joined_plane.md)
  and [source-cell refinement](research_mixed_terminal_source_cell_joined_plane.md)
  leave the same ordinary \(s\) cost and a selected \(a\) cost.
  The bare bound is paired with its original reference cell.
  Either valid terminal-side or ordinary-side marginal enclosure
  changes only the trial upper, not \(v_s\) or \(G_s\).

In each case the terminal upper function depends on \(a\) and
terminal targets, and is independent of \(r,b,c\). The only
\(b\)-dependence of its ordinary part is
\(g(s+b)-g(b)+2\pi ibs\), together with the incoming allocated
halfweight. The incoming force at the lifted reference is zero
after subtracting its original marginal.

Append \(Q(r;c,b)-g(b)/2-\gamma g(c)/2\), restore the other
incoming halfweight, and select \(b\). Original stationarity
cancels the joined complex marginal. Equations (5)--(8) then
show that its two-lift upper is
\[
\begin{split}
 \mathfrak D_{\mu,\nu,\sigma}\le{}&
 T_{b,\mu}+T_{\sigma,\nu}
 +G_r(A_r)+G_{b,\mu}(A_{b,\mu})\\
 &\hspace{32mm}+G_s(u+v_s)+R_{\sigma,\nu}\\
 \le{}&\mathfrak B_\mu+\mathfrak A_{\sigma,\nu}.
\end{split}
\tag{19}
\]
The first inequality follows by integrating the simultaneous
diagonal costs along the real target segment; the second is
Lemma 1 with the signs (11). All original target intervals remain.
The terminal real-cut target is not moved to its main height.

The original bare-source comparison is still applied only at
the actual \(a(b)\). Because \(b\in O_4\subset K_4\), its
canonical source eligibility follows from the completed terminal
theorem. Lifting the target \(b\) does not alter that reference
or its source-cell association. No bare-source result is assumed
on a new independent image rectangle.

For clarity, (18) may use exact original scalar costs even when
the saved calculation bounded them by cubic costs. The latter
remain upper bounds for the former. The common conjugate in
(19) is chosen before rounding; no convexity property of a
rounded implementation is assumed.

**Corollary 3 (only the remaining shared debit need be paid).**
Define
\[
\begin{split}
 \Delta_s&=G_s(u+v_s)-G_s(v_s),\\
 \rho&=\left(1-\frac{v_s}{-u}\right)_+\in[0,1],\\
 \widetilde{\mathfrak B}_\mu
   &=T_{b,\mu}+G_r(A_r)+G_{b,\mu}(A_{b,\mu})+\rho G_s(u).
\end{split}
\tag{19a}
\]
Then the exact extra budget in the first inequality of (19) is
\(T_{b,\mu}+G_r+G_{b,\mu}+\Delta_s\), and
\[
       \Delta_s\le \rho G_s(u),\qquad
       \mathfrak D_{\mu,\nu,\sigma}
            \le\widetilde{\mathfrak B}_\mu+\mathfrak A_{\sigma,\nu},
       \qquad
       \widetilde{\mathfrak B}_\mu\le\mathfrak B_\mu .
\tag{19b}
\]
If \(v_s\ge-u\), then \(u+v_s\in[0,v_s]\), so convexity and
\(G_s(0)=0\) give \(\Delta_s\le0\). If \(v_s<-u\), then
\(u+v_s=\rho u\), so \(G_s(u+v_s)\le\rho G_s(u)\);
subtract the nonnegative \(G_s(v_s)\). This proves (19b).
The exact signed \(\Delta_s\) may be retained when a stronger
upper bound is available. No analogous nonnegativity is imposed
on a forced \(b\)-gain whose target interval misses its center.

## 5. Uniform consequence and the remaining two inequalities

**Theorem 4.** Suppose that, for both terminal types and both
external types, on the actual filtered families,
\[
           \mathfrak B_0\le0,\qquad \mathfrak B_1\le0
                         \quad\hbox{on }\Omega^K_{\gamma,\epsilon}.
\tag{20}
\]
Then all 108 terminal comparisons for each fixed
\((\gamma,\epsilon)\) retain raw gap \(1/2600\).
The weaker hypothesis \(\widetilde{\mathfrak B}_0\le0\) and
\(\widetilde{\mathfrak B}_1\le0\) also suffices.

*Proof.* The completed
[type-four-input terminal theorem](research_mixed_terminal_uniform_kernel_completion.md)
provides for every terminal label and each alternative a valid
route in (18), with an outward upper strictly below \(-1/2600\)
throughout the actual \(K_4\) family. Apply (19) and (20),
or (19b) under the weaker hypothesis.
The route or its source cell may vary with the reference; the
pointwise inequality (19) holds for every valid choice.
The two own-four ordinary nonmain alphabets are already
dominated by their main maxima in the two-selected window.
Their losses are added, so they cannot weaken this gap.
\(\square\)

Consequently (20), if established, would bound the complete
literal source
\[
 \left|C_{1,N}(X_c,X_b)C_{1,N}(X_b,X_a)
       \mathcal V_{\epsilon,N}(w,X_a)
       d_N(X_b)X_b^{-N}d_N(X_a)X_a^{-N}\right|
                         |d_N(X_c)|^{\gamma/2}
\tag{21}
\]
by its original affine reference rate minus a finite gap
\(1/5200\), after one aggregate source tolerance and polynomial
prefactor allowance. It retains the whole terminal envelope,
both Fourier alternatives at both nodes, all real colors, small
complex color neighborhoods, fixed jets and both parities under
the same complete-source hypotheses. No conclusion for (21)
is asserted before (20) is proved.

The old selected-plateau theorem does not supply (20): it uses
the cyclic reference rectangle
\([.27,.33]+i[-.057,-.02]\), whereas the present endpoint-near
ordinary images have only the wider bounds (2) before further
correlation is used. Nor does the completed terminal gap alone
pay the new trial \(T_{b,\mu}\). The exact reconstruction and
stationarity (8) are available to prove (20) on a single old
parameter \(b\); they do not establish its sign by themselves.

Thus the new deduction is a reduction of the required uniform
comparisons to two ordinary budgets, with all terminal source
work inherited. It is not a new selected-source sign, a
full-reference cover, or a whole-word theorem.
