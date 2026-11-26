# Independent joint-charge audit for direct filled crossings

Private report, 1 November 2026. No repository file is changed.

I read `notes/general_original_source_long_filling_transfer.md` in full and reopened the exact charge and contour proofs it uses: `notes/actual_pretzel_long_filling_charge_selection.md`, Sections 2–4; `notes/actual_pretzel_cusp_corridor_filling_survival.md`, Sections 3–5; and `notes/actual_filling_source_fourier_endpoint_gap.md`, especially Section 5 and its telescoping identity (14a). I also read the direct filled-coupon report through Section 7. The purpose here is to separate the analytic charge-ordering argument, which does transfer, from the old auxiliary-basis filling identity, which cannot simply be reused at a moving main meridian.

## 1. What a direct wire packet must supply

Let there be \(b\) filled physical circles and fixed signed nonzero integers \(n_i\), with \(n_i=\epsilon_i-2p_i\) in the retained convention. A suitable direct finite wire packet is a specified finite holomorphic function \(\mathcal B_N(\tau,s)\), before multiplying the factors
\[
 \prod_{i=1}^b\sin\tau_i\,
       \exp\left(\frac{iNn_i\tau_i^2}{4\pi}\right).
 \tag{1}
\]
Its defining finite wire indices, cutoffs, factorial interpolation, type scalars and endpoint currents must be fixed by the source. A recurrence solution or a pointwise real-grid asymptotic is not a substitute.

The following properties are sufficient for the local multicharge analysis.

1. On a fixed complex neighborhood of a real central cube, \(\mathcal B_N\) is exactly even in each \(\tau_i\), and it has a uniform analytic asymptotic
\[
 \mathcal B_N(\tau,s)
 =N^\nu a(\tau,s)e^{N\mathcal B(\tau)}(1+O(N^{-1})).
 \tag{2}
\]
The leading amplitude is nonzero on a smaller neighborhood, and both it and the action are separately even. The exact finite packet, not the relative error in (2) treated as an independent arbitrary function, is used in all contour moves.

2. The action has
\[
 \mathcal B(0)=F_0,\qquad
 \mathcal B''(0)=-\operatorname{diag}(a_1,\ldots,a_b),
 \qquad a_i>0,
 \tag{3}
\]
and a fixed complex Gaussian bound of the form
\[
 |\mathcal B_N(x+iy,s)|
 \le N^C\exp N(F_0-c\|x\|^2+C'\|y\|^2).
 \tag{4}
\]
For the direct Newton construction, exact evenness follows from the literal products \(\mathcal E_N(x,\tau_i)\). It also makes every mixed wire–\(\tau_i\) derivative vanish at zero. Thus elimination of the strict wire saddle does not create off-diagonal terms in (3): the candidate curvature is
\[
 a_i=\frac1{2\pi}\sum_{e\sim i}\tan(\pi x_e^*)>0.
 \tag{5}
\]
Equation (5) follows only after the actual strict wire packet has been constructed. The known negative original wire Hessian gives its local nondegeneracy, not its exact finite contour by itself.

3. The exact direct root-grid trace admits the coordinatewise translated-rectangle identity with all currents retained. Its paired charges have \(\ell_i\ge1\), with coefficients
\[
 \prod_i\eta^{\ell_i-1}
       U_{\ell_i-1}(\cos2\pi s_i),
 \tag{6}
\]
where \(s_i=s\) on a moving same-color object and the constant-order counterpart is retained on the other type. The first coefficient in every coordinate is exactly one. Separate oddness after including \(\sin\tau_i\) removes the central real zero-mode integral, but leaves endpoint currents that require their own estimate. The direct one-variable report proves this identity; a multivariable use must keep the spectator variables and their derivatives controlled.

4. Outside the central wire/angle windows and in the paired endpoint currents there is a fixed loss below \(F_0\), uniformly while the other variables remain on their original real grids or finite real contours. Exact telescoping of the coordinate functionals removes their tails before any other chirp is moved off its real contour. Fixed powers of the \(n_i\) in polynomial prefactors are allowed; \(\exp(N|n_j|)\) costs from complex spectator chirps are not.

The original general transfer assumes counterparts of these properties for the actual auxiliary-color packet and proves its own exact Hermite filling transform. That transform is not the direct \(R_s^{n_i}\) transform. The direct proof must establish item 3 from its actual crossing eigenvalues and trace, as the local report does, and verify item 4 for its new packet. The analytic mechanism below then applies without changing its source.

## 2. An exact local charge-ordering lemma

Assume (2)–(3). For a positive charge vector \(\ell\), the direct critical action is
\[
 S_{\ell,n}(\tau)=\mathcal B(\tau)+
       \frac{i}{4\pi}\sum_i n_i\tau_i^2-i\sum_i\ell_i\tau_i.
 \tag{7}
\]
Put \(\varepsilon_i=1/n_i\), \(t_i=\ell_i/n_i\). Its critical equation is
\[
 \tau_i=2\pi t_i+2\pi i\varepsilon_i\mathcal B_i(\tau).
 \tag{8}
\]
The implicit-function theorem at \((t,\varepsilon,\tau)=0\) gives one holomorphic solution on a fixed polydisk, with \(\tau(t,0)=2\pi t\). The components of \(\varepsilon\) may have independent signs and magnitudes.

Complete the square in (7). At this solution,
\[
 S_{\ell,n}(\tau_*)
 =-i\pi\sum_i\frac{t_i^2}{\varepsilon_i}
                 +\widehat{\mathcal B}(t_1^2,\ldots,t_b^2,\varepsilon).
 \tag{9}
\]
The remainder is holomorphic even when an \(\varepsilon_i\) is zero. One explicit expression before changing to squared coordinates is
\[
 \mathcal B(\tau_*)
      -i\pi\sum_i\varepsilon_i\mathcal B_i(\tau_*)^2.
 \tag{10}
\]
Indeed \(\tau_i-2\pi t_i=2\pi i\varepsilon_i\mathcal B_i\), and the quadratic completed-square term is \(-i\pi\varepsilon_i\mathcal B_i^2\). Uniqueness of (8) and separate evenness of \(\mathcal B\) imply that (10) is even in each \(t_i\), justifying (9).

At \(\varepsilon=0\), the remainder is \(\mathcal B(2\pi t)\). Consequently
\[
 \partial_{t_i^2}\operatorname{Re}
       \widehat{\mathcal B}(0,0)=-2\pi^2a_i.
 \tag{11}
\]
Shrink one fixed real box in \((t^2,\varepsilon)\) so that each derivative is at most \(-\pi^2a_i\). For every independently sufficiently long fixed signed \(n_i\), and every local charge with \(|\ell_i/n_i|\le t_0\), integrate these inequalities from \(1/n_i^2\) to \(\ell_i^2/n_i^2\), one coordinate at a time. The first term of (9) is purely imaginary on these real parameters. Therefore
\[
 \boxed{\displaystyle
 \operatorname{Re}S_{\ell,n}(\tau_\ell)
 \le\operatorname{Re}S_{\mathbf1,n}(\tau_{\mathbf1})
       -\pi^2\sum_i a_i\frac{\ell_i^2-1}{n_i^2}.}
 \tag{12}
\]
The rightmost loss is positive for every nonminimal charge. It may be very small for an extremely long fixed slope, but it remains a strictly positive exponential loss as \(N\to\infty\). No comparability of the \(n_i\) appears in its proof.

Separate evenness gives \(\mathcal B_i(\tau)=\tau_iQ_i(\tau_1^2,\ldots,\tau_b^2)\). Hence (8) also gives the componentwise exact factorization
\[
 \tau_i=
 \frac{2\pi t_i}{1-2\pi i\varepsilon_iQ_i(\tau^2)}.
 \tag{13}
\]
For real \(t,\varepsilon\), this proves
\(\operatorname{Im}\tau_i=O(|\varepsilon_i t_i|)\), after shrinking the fixed box. It also proves \(\tau_i\ne0\) for nonzero charge, so the local amplitude factor \(\prod_i\sin\tau_i\) does not vanish. The real part of the Hessian of (7) on the translated real contour remains strictly negative: the filling Hessian is purely imaginary, and \(\mathcal B''\) is close to the negative matrix in (3). The Gaussian coefficient is nonzero for all slope signs.

These are the exact analogues of the squared-charge argument and componentwise connector bound in the original transfer. The scales and constants differ because (7) uses \(n_i\tau_i^2/(4\pi)-\ell_i\tau_i\), rather than the old \(-2\pi(p_iz_i^2+m_iz_i)\).

## 3. Why the separate first-alias errors are insufficient

This limitation is already visible in a diagonal quadratic action and is not a counterexample to charge ordering. Set
\(\mathcal B(\tau)=F_0-\frac12\sum_i a_i\tau_i^2\). Then exactly
\[
 \operatorname{Re}S_{\ell,n}(\tau_\ell)
 =F_0-2\pi^2\sum_i
     \frac{a_i\ell_i^2}{n_i^2+4\pi^2a_i^2}.
 \tag{14}
\]
Take \(n_1=T\), \(n_2=T^2\), with \(T\) large but fixed before \(N\). The all-first action loses order \(T^{-2}\) from \(F_0\), whereas the second coordinate's separate higher-alias gap is only order \(T^{-4}\). Thus an absolute error bounded at \(F_0-cT^{-4}\) need not lie below the filled first action. No threshold requiring only both individual slopes to be large reverses this comparison.

Nevertheless (12), or directly (14), shows that the joint charge \((1,2)\) loses a positive amount of order \(T^{-4}\) *relative to* \((1,1)\). This is the comparison needed in the whole signed integral. It is why all joint charges must be retained until their common wire saddle and action have been formed.

## 4. Nonlocal charges and endpoint currents

The local lemma does not alone control the full charge sum. The old proofs use two distinct estimates, both of which are required for the direct packet.

First remove high-charge tails by an exact telescoping identity for the coordinate functionals. While a tail is removed in coordinate \(i\), every spectator remains on its real grid or on a finite real contour. Its chirp then has modulus one; fixed derivatives cost only powers of \(N\) and the fixed slopes. The direct translated kernel has geometric horizontal tails and bounded vertical kernel (its exact formula (13)); the paired zero-mode and endpoint currents must still be kept together. This argument must be made for the actual finite \(\mathcal B_N\), uniformly in the real spectators and the fixed mixed derivatives required by the remaining functionals. It cannot use the old beta-coefficient identity as a substitute.

After this reduction only finitely many charges remain for each fixed slope tuple. For a nonlocal charge with \(|\ell_i/n_i|\ge t_0\), split its real coordinate into a smaller central interval and its complement. The complement has the fixed source Gaussian loss. On the central interval, \(n_i\tau_i/(2\pi)-\ell_i\) has a fixed sign and magnitude of order \(|n_i|t_0\). A fixed small imaginary shift in that coordinate decreases the phase. The bounded normal derivative of the source action cannot overcome it for long \(|n_i|\). Connector starting points already have the source loss. The shift and its estimate involve only \(n_i\), not the largest other slope.

For local charges, translate to the saddle using (13). It gives \(|n_i\operatorname{Im}\tau_i|\le C|t_i|\) and \(|\ell_i\operatorname{Im}\tau_i|\le Ct_i^2\), so all endpoint connectors stay below the central action after choosing the local charge cube small. The actual finite analytic packet then has the nonzero Gaussian evaluation, and (12) orders the resulting critical actions.

Finally the all-first action tends to \(F_0\) uniformly as \(\max_i|1/n_i|\to0\). A single lower bound on every \(|n_i|\) therefore places it above every *fixed* wire, angular, high-sector and endpoint loss. These fixed losses, unlike separate local alias gaps, can be compared with the total filled action drop. This distinction is essential.

## 5. Exact phases, parity, and the present remaining input

In the direct paired contour, the two signs of each charge have already combined into (6). The first coefficient is exactly one at every parity and every main parameter, including its removable collision values. Thus no leading sign cancellation remains to be excluded by an informal analogy with the old \(m\sinh\) kernel. The nonzero \(\prod_i\sin\tau_{*,i}\) and the Gaussian branch are fixed by the actual contour. All Cartan factors \(q^{n_i(d^2/4-s^2/2)}\), typed edge factors, and the original framing/closing ratio remain outside or inside the packet as their exact ledger specifies. They cannot be absorbed into a fitted normalization.

The scalar factor \(U_{\ell_i-1}(\cos2\pi s)\) can grow with \(\ell_i\), but only exponentially in the fixed parameter radius. The geometric high-charge horizontal decay overcomes this for large \(N\); each remaining finite charge has an \(N\)-independent bounded coefficient. Its first coefficient stays one. The same-color collision removal must be applied to the whole analytic difference on a parameter circle, as in the one-variable direct report, not separately to current terms with displayed sine denominators.

The local joint-charge lemma (12) is proved above. The remaining substantive source input is the actual grouped finite wire packet with uniform complex interpolation and the real-spectator endpoint/tail estimate in item 4. Its strict Hessian and separate evenness are supported by the exact Newton factors and the original complete state, but neither property alone proves the whole finite contour statement. Once that packet and its retained-current estimate are supplied, the old analytic charge-selection mechanism applies with the direct constants above. The resulting action is the original marked filling action by the exact identity \(n_i=\epsilon_i-2p_i\), not by a quadratic Hessian comparison.

No whole filled equality is asserted by this report before those source interfaces are written and checked.

## 6. Check of the written joint transfer and its tail construction

After writing the preceding independent derivation, I read `/private/tmp/md-joint-filled-chirp-transfer-and-independent-slopes.md` in full, in the version with SHA256 `350ecc539273b5d4e1ba7510b17dd76949d9e9599d3a3035ed0c3fab6fc2296d`. Its conditional argument satisfies the requirements above. In particular, its Section 3 supplies the real-spectator tail construction, assuming the stated global finite-packet Gaussian bound.

The choice \(L_i=\lfloor t_0|n_i|\rfloor\), \(y_i=A_0t_0/|n_i|\) gives, at every omitted charge, the rate loss
\[
 t_0^2\left(A_0-\frac{A_0^2}{16\pi^2c}
                         -\frac{CA_0^2}{n_i^2}\right)
                         \ge A_0t_0^2/2.
\]
This is a fixed source loss, rather than a loss of order \(n_i^{-2}\). The coefficient growth in the charge index is independent of \(N\) and is dominated by the remaining geometric decay for each fixed slope tuple. Original vertical currents cost only \(O(Nt_0)\) in the chirp exponent; retained-charge endpoint connectors cost \(O(Nt_0^2)\). Both are absorbed by the fixed endpoint angular loss after choosing \(t_0\) small.

The exact telescoping product leaves every spectator on a real finite integral or an original grid shifted by \(O(N^{-1})\). On the latter, its fixed-power chirp has bounded modulus depending on that fixed slope, not a positive rate proportional to \(N|n_j|\). Thus the independently unequal slopes do not spoil the one-coordinate estimates. The introduction of formal independent grid parameters is legitimate for these polynomial trace functionals. The final maximum principle applies to the whole holomorphic difference, so it restores the ordinary collision values without separately declaring individual divided currents removable.

Its joint critical equations, squared-charge inequality, componentwise downward heights, and nonzero first coefficient agree with Sections 2–5 above. The real Hessian on the translated local box stays negative definite, and its endpoint connectors are controlled by the componentwise heights, not by a common height involving the largest slope. The first-charge coefficient is exactly one after the signs have been paired. The actual marked action and every Cartan, edge and framing factor remain explicit.

The polynomial power also checks independently. If there are \(P\) bare vertices, \(m\) circle vertices, \(E=P+m-1\) retained edges, and \(I=\sum_{v\text{ bare}}(d_v-3)\) hidden bare variables, then there are \(E+I\) free wire integers and \(I+P\) complete gate factors. The number of circle Newton incidences is \(2E-I-3P\). Each gate costs \(N^{-3/2}\), each circle incidence costs \(N^{-1}\), and the wire Gaussian contributes \(N^{(E+I)/2}\). The resulting exponent is \(3(1-m)/2\). The \(m\) traces and angular Gaussian integrations then restore \(N^{3/2}\). This count uses the actual grouped lattice, not an unchanged assertion of the original primitive dimension.

Accordingly the written joint transfer is valid as a theorem conditional on its explicit finite wire-packet and grouped global-error hypotheses. Its tail argument is now supplied at that conditional level. The remaining source check is the construction of that packet and its bounds from the literal Conway source; the conditional transfer itself does not infer them merely from the geometric maximum.
