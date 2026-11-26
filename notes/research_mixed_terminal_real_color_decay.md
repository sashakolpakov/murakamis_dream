# Real outside-color decay for both complete terminal transforms

Research deduction, 5 November 2026. The completed terminal source
comparisons extend to the whole real ordinary-color period, with a
strict angular loss relative to the original action or supporting
plane. The argument keeps the complete endpoint coefficients on their
contours. It separately checks the upper Newton rows and uses the
physical support to avoid an unwarranted off-grid endpoint extension.
No numerical execution or new source comparison is required.

## 1. Statement and original allocation

Let \(a_*=A+iH\) be an actual incoming nonprivate leg of a terminal
vertex in a fixed mixed three/four word of length \(m\ge2\).
Write the terminal type as \(3+\epsilon\), and the incoming type
as \(3+\nu\), where \(\epsilon,\nu\in\{0,1\}\).
Keep its original action \(\mathcal P_\epsilon\), critical point,
and logarithmic lifts. Put
\[
\begin{split}
 P&=[.22,.45],\qquad \kappa=1/2500000,\qquad d=y-A,\\
 B_{\epsilon,0}(a_*;y)
 &=\Re\mathcal P_\epsilon(a_*)+
       \Re\mathcal P_\epsilon'(a_*)d-\kappa d^2,\\
 \Pi_{\epsilon,\nu}&=\mathcal P_\epsilon-\nu g/2,\\
 B_{\epsilon,\nu}(a_*;y)
 &=\Re\Pi_{\epsilon,\nu}(a_*)+
       \Re\Pi_{\epsilon,\nu}'(a_*)d-\kappa d^2,
 \qquad D(\theta)=1-\cos\theta.
\end{split}                                                    \tag{1}
\]
The target is \(a=y+iH\), with its actual unselected height.
For \(\nu=1\) one has \(H<0\). Reference coverage, including
the opposite attached leg when \(m=2\), is precisely that of
[the completed mixed plateau theorem](research_mixed_full_unselected_plateau.md).
In particular the type-four source uses its proved necessary feasible
domain, not an enlarged independent input disk.

**Theorem 1.** There are \(c>0\) and polynomial prefactors such that
both terminal types, both level parities, all these actual references,
and all independent \(y\in P\) satisfy
\[
 |V_{\epsilon,N}(-2\cos\theta,e^{-2\pi ia})|
 \le C N^A
 e^{N\{B_{\epsilon,0}(a_*;y)-cD(\theta)\}},
       \qquad-\pi\le\theta\le\pi .
                                                               \tag{2}
\]
Consequently the literal unselected halfweight gives
\[
 |V_{\epsilon,N}(-2\cos\theta,e^{-2\pi ia})|
 |d_N(e^{-2\pi ia})|^{\nu/2}
 \le C N^A
 e^{N\{B_{\epsilon,\nu}(a_*;y)-cD(\theta)\}}.
                                                               \tag{3}
\]
Every fixed ordinary-color derivative obeys the same exponent, with
a larger polynomial prefactor. At \(y=A\), the bare reference rate
in (2) is exactly \(\Re\mathcal P_\epsilon(a_*)\).

The proof below uses the completed source partitions. The previously
conditional type-four assembly is discharged by Corollary 3 of the
mixed plateau theorem and its complete saved replay. Its analytic
partition is retained unchanged apart from deleting terms which are
identically zero before any deformation.

## 2. Uniform real-color bounds needed at physical endpoints

Write \(w=-2\cos\theta\), and use the original Newton entropy
\(V_\theta(u)\). The
[endpoint real-color theorem](research_mixed_endpoint_real_color_decay.md) proves
\[
 \begin{split}
 |C_N(e,w)|&\le C N^A e^{N\{\Re S(e)-c_E D(\theta)\}}
       &&\text{on } E_c=[.27,.49]+i[-.055,.04],\\
 |H_N(w,r^{-j})|&\le C_I N^{A_I}e^{N h(j/N)}
       &&(j/N\in I\Subset(0,1)),\\
 h(e)&=J(e)+\lambda(e),\qquad \lambda(e)=\Re S(e).
 \end{split}                                                   \tag{4}
\]
The second line drops a favorable angular loss. It is a physical-index
bound for the whole coefficient. Also
\[
 V_\theta(u)\le V_0(u)\quad(0\le u\le1/2),\qquad
 V_\theta(u)\le0\quad(1/2\le u\le1),
 \quad \max_u V_\theta(u)\le b_2<3/5.
                                                               \tag{5}
\]
All these estimates are for exact polynomials, including their zeros.

Here are two endpoint consequences used in both terminal partitions.

**Lemma 2.** The coherent cap seam ceilings
\(b_0=101/125\), \(b_1=433/500\) and the strict terminal
end-index ceiling \(217/250\) remain valid uniformly for every real
ordinary color, with an arbitrarily small total finite-rate tolerance.
Each removed end-index row retains its entire private and Newton sums.

*Proof.* In [the cap seam proof](research_mixed_cap_seam_source_bounds.md),
the compact private rows are bounded by
\(|C_N(j/N,w)|S_j^{1-\epsilon}\). Equation (4), with
\(|C_N|=|H_N|/S_j\) at physical indices, retains their rates
\(\lambda(e)+(1-\epsilon)J(e)\) at every real color.
The old scalar maxima are therefore unchanged. For \(e\le.01\),
the literal coefficient has only Newton rows \(u\le e<1/2\),
so (5) preserves its old endpoint bound. For \(e\ge.99\),
the exact reflected-factorial inequalities in that proof use only
\(\sum_l|e_l(w)|\le\operatorname{poly}(N)e^{Nb_2}\).
Equation (5) supplies precisely this bound. Thus the positive sum of
the moduli of whole coherent coefficients has the same seam ceilings.
The zero-safe estimate for \(p_j(e^{-2\pi ix})/P_j\) extends
them to the same small real outgoing collar, with cost
\(\Delta_\delta=\delta\log2-J(\delta)\to0\).

For the terminal transform retain exactly
\[
 V_{\epsilon,N}(w,X)=\sum_{i<N}
 \frac{X^{-i}p_i(X)}{P_i^{1+\epsilon}}U_{\epsilon,N}(w,r^i).
                                                               \tag{6}
\]
Its outer coefficient has the same zero-safe rate
\(\chi_\epsilon(t,a)\) as in
[the terminal end-tail theorem](research_mixed_terminal_transform_tails.md),
with \(\chi_\epsilon(0,a)=0\) and
\(\chi_\epsilon(1,a)=2\pi(-\Im a)_+\le.24\pi\).
The preceding seam bound handles \(t=i/N\le\delta\).
For \(t\ge1-\delta\), the exact support of the whole physical
cap restricts its private index to \(0\le e=j/N<1-t\le\delta\)
and its Newton index to \(0\le u=l/N\le e\). Every such
Newton row is below one half. Its original absolute entropy, before
the outer coefficient, is at most
\[
 V_0(u)-J(u)-J(e-u)+J(t+e)-J(t)-\epsilon J(e).
                                                               \tag{7}
\]
This tends uniformly to zero as \(t\uparrow1\), since
\(J\) and \(V_0\) have continuous zero endpoint values on
this support. The original uniform finite-product bounds are valid
through all zeros. Choose \(\delta\) and then a common tolerance
as in the end-tail theorem. The lower tail has rate below
\(.866+.002=.868\); the upper tail has rate below
\(.24\pi+.002<.868\). The positive outer-row majorant, still
with whole cap values, has the stated bound. \(\square\)

For later type-four private tails we need only the following weaker
whole-period assertion, whose upper endpoint is cut off by exact support.
For every fixed \(\delta>0\) and \(\eta>0\),
\[
 |H_N(w,r^{-j})|\le C_{\delta,\eta}N^{A_{\delta,\eta}}
 e^{N\{h(j/N)+\eta\}},\qquad 0\le j/N\le1-\delta,
 \quad w\in[-2,2].
                                                               \tag{8}
\]
Indeed (4) proves it on every compact subinterval away from zero.
For a small physical \(e=j/N\), the exact positive coefficient
bound has entropy
\[
 J(e)+V_\theta(u)-J(u)-J(e-u)
 \le J(e)+2u\log2-3J(u)-J(e-u),\qquad0\le u\le e.
                                                               \tag{9}
\]
Its supremum tends to zero as \(e\downarrow0\), uniformly in
\(\theta\). The known function \(h\) is nonnegative and
continuous with \(h(0)=0\), as proved in
[the endpoint collar theorem](research_mixed_endpoint_polynomial_collar.md),
Section 3. A small fixed low interval followed by a compact interval
therefore proves (8). This argument makes no assertion about an
off-grid all-real-color \(H_N\) near its other period endpoint.

## 3. Type three: the upper Newton rows retain the old scalar ceiling

The literal type-three source is
\[
 V_{0,N}(w,X)=N\sum_{i+l<N}(-q)^{-l}e_l(w)
           \frac{X^{-i}p_i(X)P_{i+l}}{P_i^3P_l^2}.
                                                               \tag{10}
\]
For upper Newton rows put \(u=l/N\ge1/2\), \(t=i/N\le1-u\),
\(v=1-u\), and \(L=-J\) on \([0,1/2]\). By (5), their
zero-safe absolute entropy is bounded by
\[
 \begin{split}
 &V_\theta(u)+J(u+t)-2J(u)-3J(t)+Q_a(t)\\
 &\qquad\le L(v-t)-2L(v)+3L(t)+Q_a(t)\\
 &\qquad\le L(1/2-t)+3L(t)+c_*t,
 \qquad c_*=\log(1+e^{.24\pi}).
 \end{split}                                                   \tag{11}
\]
Here \(Q_a\) is the exact external-product/chirp rate. The last
line uses \(Q_a(t)\le c_*t\), \(L(v)\ge0\), and
\[
 L(v-t)-L(v)=J(v)-J(v-t)
                  \le J(1/2)-J(1/2-t)=L(1/2-t).
                                                               \tag{12}
\]
Thus the same already checked scalar ceiling in
[the upper Newton theorem](research_mixed_terminal_three_high_newton.md)
applies, although the complete-color entropy of the upper Newton
factor itself is not an upper bound for general colors:
\[
 \max_{0\le t\le1/2}\{L(1/2-t)+3L(t)+c_*t\}
 <\frac{95458861}{108769600}<.878.
                                                               \tag{13}
\]
The positive upper-half double sum consequently has finite rate
\(.879\), uniformly over the real outside color period.

Now follow the exact partition in
[lower-half completion](research_mixed_terminal_three_rectangle_completion.md)
and [whole type-three completion](research_mixed_terminal_three_full_completion.md).
Remove the complete lower end-index sector first using Lemma 2.
The low Newton and near-half Newton positive bounds are unchanged
by \(V_\theta\le V_0\) below one half. Equation (11) handles
the entire upper Newton half. All have the old strict bare gap,
since the reference plane exceeds \(.89\), whereas these positive
ceilings are below \(.879\).

Every remaining Newton contour lies in a fixed compact strip
\(0<\Re u<1/2\). Apply the exact factorial boundary inequality,
equation (3) of the endpoint real-color theorem, to its Newton factor
before taking any integral. The remaining original density is color
independent. The main two-index horizontal current therefore gains a
uniform \(c_0D(\theta)\) loss from its calibrated bare plane.
Every mixed join, both types of single alias, every double alias,
and the one-index left and Newton exterior strips retain their old
complete-color bounds and strict gaps. Transport the complete-color
upper phase to its old anchor before using the old height convexity;
no derivative inequality for a far-color critical action is asserted.
The real left corners use (5). Half-grid cut slivers remain on the
same regular compact sets, and the even \(i=N/2\) column is kept
exactly as in the original partition.

For \(t=i/N>1/2\), the support in (10) forces
\(u<1-t<1/2\). Equation (5) therefore preserves the positive
[right-triangle bound](research_mixed_terminal_three_right_triangle.md)
and its completed raw half-face gap. This covers all remaining rows.
It does not restrict an inner sum previously bounded only coherently.

## 4. Type four: use whole coefficients and the support wall

Use exactly the square source of
[the type-four completion](research_mixed_terminal_four_full_completion.md):
\[
 V_{1,N}(w,X)=\sum_{i,j<N}
 \frac{X^{-i}p_i(X)}{P_i^2}
 \frac{p_j(r^i)H_N(w,r^{-j})}{P_j^2}.
                                                               \tag{14}
\]
All physical terms with \(i+j\ge N\) vanish, at every color.
Choose \(0<\delta<.01\). First remove its entire
\(i\le\lfloor N\delta\rfloor\) sector by Lemma 2,
with its full inner sums. Set
\(i_{\min}=\lfloor N\delta\rfloor+1\).
For every remaining physical \(i\), all columns
\(j\ge N-i_{\min}\) vanish. Delete only these entire columns.
Every retained column then satisfies
\[
             0\le j<N-i_{\min},\qquad j/N<1-\delta.
                                                               \tag{15}
\]
This fixed column deletion is made before any contour deformation;
it leaves the central private rectangle unchanged for all sufficiently
large levels. Within each retained column keep the literal
\(p_j(e^{-2\pi it})\) on the full transform residue rectangle.
Its row-dependent physical support zeros may revive off grid and
are not deleted or set to zero there. This is why (8), rather than an unproved off-grid
all-color endpoint collar theorem, suffices for all remaining physical
private indices. The private index stays physical in every private-tail
or real-corner estimate; only its transform variable is interpolated.

On the central private rectangle \(E_c\), the reduced double
interpolant retains the complete \(C_N(e,w)\). Equation (4)
therefore bounds each original density by its complete reduced phase
with the extra \(c_E D(\theta)\) loss. Its horizontal-horizontal
current is below the original reference bare plane. The eight
flattened tests and twelve penalized alias tests retain their completed
strict margins, along with every vertical and mixed join. This uses
the original exact coefficient on the entire contour, not a bound
for a canceled leading term.

In the two private tails use (8) on precisely the surviving physical
indices (15). Their rate is the same
\(\lambda(e)-J(e)+I_t(e)\) as in
[the coherent private-tail theorem](research_mixed_terminal_four_private_tails.md),
up to an arbitrarily small common tolerance. Its monotonicity carries
the upper rate to \(e=.27\) or \(.49\), where the completed
flattened faces, corners and transform aliases apply. The polynomial
\(p_j(e^{-2\pi it})\) is kept literal, including its revived
off-grid values. Only the globally deleted columns in (15) remain
absent after deforming \(t\); no triangular support rule is imposed
on a complex transform index.

The [left transform strip](research_mixed_terminal_four_left_strip.md)
likewise keeps whole \(H_N\). Its central private currents use
(4); its low and high real private corners use (8). The original
monotonicity transports each density to its completed real anchor,
with the same strict gap and without a new raw face. The limits at
private index zero are included by (9).

Finally, for \(t=i/N\ge1/2\), the exact physical support gives
\(0\le u=l/N\le e=j/N<1-t\le1/2\). Equation (5) preserves
every row of the positive
[type-four right triangle](research_mixed_terminal_four_right_triangle.md).
Its completed raw half-face comparison pays this entire sector.
The even half-row belongs to this sector only. Thus all original
rows, both parities, all revived contour products and all original
private alternatives are accounted for.

## 5. Calibrating the loss and taking derivatives

The preceding proofs give, for either type, a bound of the form
\[
 |V_{\epsilon,N}(-2\cos\theta,e^{-2\pi ia})|
 \le C N^A\left[
 e^{N\{B_{\epsilon,0}(a_*;y)-c_0D(\theta)\}}
             +e^{N\{B_{\epsilon,0}(a_*;y)-\gamma\}}\right]
                                                               \tag{16}
\]
with \(c_0,\gamma>0\). The second term includes all restored
physical sectors and nonprincipal currents. Choose all finite-product
and endpoint-envelope tolerances once, strictly below the minimum of
their completed positive reserves, before fixing \(\gamma\).
The constants may be made common on the stated actual-reference
families. Since \(D\le2\), take
\(0<c\le\min(c_0,\gamma/2)\) to prove (2).

For the unselected incoming type-four halfweight, \(H<0\) and
its rate is \(-\Re g(y+iH)/2\). The same horizontally convex
remainder as in the completed terminal theorem gives
\[
 B_{\epsilon,0}(a_*;y)-\frac\nu2\Re g(y+iH)
                      \le B_{\epsilon,\nu}(a_*;y).
                                                               \tag{17}
\]
This proves (3) with the literal finite weight and its polynomial
prefactor. Neither a Fourier zero nor a source value is divided out.

Each whole \(V_{\epsilon,N}\) has ordinary degree less than \(N\).
The weighted disk maximum principle used in the endpoint real-color
theorem therefore extends (2) with at most
\((1+c)|\Im\theta|\) rate cost. On ordinary-color circles of
radius \(N^{-2}\), the inverse angle changes by \(O(N^{-1})\),
uniformly through both angular branch points. Cauchy's formula proves
all fixed ordinary derivative estimates in (2)--(3) with polynomial
cost. It is applied after proving the whole-source real bound.

At the actual incoming target the already completed nonzero local
packet has the original angular Hessian
\[
 \left.\partial_\theta^2
 \mathcal P_\epsilon(a_*,-2\cos\theta)\right|_{\theta=0}
              =-\frac{\tan(\pi u_*)}{2\pi},\qquad
                         \Re\tan(\pi u_*)>0.
                                                               \tag{18}
\]
Thus the one-variable patching lemma of
[the stability reduction](research_mixed_open_source_stability_reduction.md)
also gives, on a fixed thin angular strip at this actual target,
\[
 |V_{\epsilon,N}(-2\cos(\theta+i v),e^{-2\pi ia_*})|
 \le C N^A e^{N\{\Re\mathcal P_\epsilon(a_*)
                       -c'(1-\cos\theta)+Bv^2\}}.
                                                               \tag{19}
\]
No moving critical packet is asserted on all independent plateau targets.

Both endpoint factors now have calibrated real outside-color decay on
the unselected plateau. Combining them with the color-independent
ordinary factors transfers the two losses through that specified
sector. The whole open polynomial still requires its remaining
selected and nonplateau source comparison uniformly in the outside
colors. No value of a canceling whole-word sum supplies that comparison,
and this endpoint result does not identify the marked geometric germ
or prove stability under arbitrary short partial fillings.
