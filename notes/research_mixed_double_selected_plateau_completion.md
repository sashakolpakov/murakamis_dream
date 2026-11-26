# The first two retained selections and arbitrary mixed suffixes

Research theorem, 6 November 2026. The completed double-selection
comparison joins the first-only and second-only theorems with arbitrary
later types, including the terminal factor at length four. Every
nonempty type-compatible selection supported on the first two retained
positions and the safe interior has a common finite-source gap
\(1/6400\). Their partial plateau sum retains the original nonzero
geometric coefficient. The whole invariant is not asserted here.

## 1. The original three-factor product and its completed comparisons

Fix a mixed word of length \(m\ge4\) with first three flags
\((1,1,\beta)\), \(\beta\in\{0,1\}\). Write its original
retained references as \(r_j=a_j+ic_j\). Put \(P=[.22,.45]\),
\(H=1/100\), and use the target heights
\[
 z_1=x_1+iH,\qquad z_2=x_2+iH,\qquad z_3=x_3+ic_3,
 \qquad (x_1,x_2,x_3)\in P^3,
 \qquad X_j=e^{-2\pi iz_j}.
 \tag{1}
\]
The literal weighted local product is
\[
 \mathcal B_{123,N}=
 |U_{1,N}(w_L,X_1)C_{1,N}(X_1,X_2)C_{\beta,N}(X_2,X_3)
     d_N(X_1)X_1^{-N}d_N(X_2)X_2^{-N}|
                           |d_N(X_3)|^{\beta/2}.
 \tag{2}
\]
Both selected weights are the complete original polynomials with
integer powers. The outgoing halfweight is a nonnegative root of a
modulus, not a holomorphic root; for \(\beta=0\) it is defined to
be one. No polynomial is divided out, including at its zeros.

Using the original cap phase and bare ordinary phases, set
\[
 \begin{split}
 F_{123}(e,z_1,u,z_2,v,z_3)
   ={}&\Psi(e,z_1)+Q_1(u;z_1,z_2)+Q_\beta(v;z_2,z_3)\\
      &-g(z_1)-g(z_2)-\tfrac\beta2g(z_3),\\
 p_R&=g'(v_*+r_3)-(1+\beta/2)g'(r_3),\\
 \Lambda_{123}&=\Re F_{123,*}+\Re\{p_R(z_3-r_3)\}.
 \end{split}
 \tag{3}
\]
Here \(u_*=s_2^*\), \(v_*=s_3^*\) are ordinary also when
\(m=4\). The first cap uses its original private coordinate,
canonical auxiliary lift and additive phase normalization.
All five internal derivatives of \(F_{123}\) vanish at the
original reference. There is one outgoing marginal and no incoming
boundary tangent after the cap has been included.

The [double-selected last-row theorem](research_mixed_double_selected_last_rows.md)
pays every outgoing last-row term with a raw gap greater than
\(3/1000\). It leaves sixteen profile/Fourier choices for prefix
\(443\) and eight for \(444\), after the completed pointwise
outgoing-four half-row domination. Denote their exact maximum defect
by \(\mathcal D_\beta\), as in equation (12) of that theorem.

The [completed tangent comparison](research_mixed_double_selected_tangent_completion.md)
proves
\[
                  \mathcal D_\beta<-\frac1{100},
                  \qquad \beta=0,1,
\]
uniformly on the original canonical families over both external
reference domains and all targets in (1). It uses all 1,431 certified
reference cells, 17,728 original profile/Fourier bounds and all eighteen
complete boundary trees. The only boundary response is
\(|p_R'b_*'|\); the incoming derivative has become internal after
including the cap. The
[one-boundary extension](research_mixed_double_selected_boundary_extension.md)
and [concave profile budget](research_mixed_double_selected_concave_profile_budget.md)
retain the original references and full target boxes.

Together with the last-row comparison, this gives
\[
                    d_{12}=\min\{3/1000,1/100\}=3/1000.
 \tag{4}
\]
The complete finite-current reduction then gives, for every
\(\tau>0\) and fixed ordinary-color derivative order \(k\),
\[
 \mathcal B_{123,N}^{(k)}
 \le C_{\tau,k}N^{A_{\tau,k}}
                  e^{N\{\Lambda_{123}-d_{12}+\tau\}}.
 \tag{5}
\]
The derivative acts on the original holomorphic integer-weighted
product inside (2), before taking its modulus and then adding the
outgoing modulus halfweight. All cap aliases, ordinary currents,
real rows, joins and both level parities are included. A sufficiently
small fixed ordinary-color disk is available. With \(\tau<d_{12}/2\),
the polynomial can be absorbed for sufficiently large \(N\), leaving
the finite-source loss \(d_{12}/2=3/2000\).

## 2. Exact matching to every suffix, including length four

Let \(h=m-1\), \(k_4=\sum_{j=1}^m\epsilon_j\), and let
\(\phi_j\) be the original allocated ordinary phases. The full
terminal phase is \(\Pi=\mathcal P_{\epsilon_m}-\epsilon_hg/2\).
The original critical action has the exact decomposition
\[
 \mathcal F_m(z_*)=F_{123,*}
       +\sum_{j=4}^{h}\phi_j(r_{j-1},r_j)+\Pi(r_h).
 \tag{6}
\]
The sum is empty for \(m=4\). The remaining derivative identities are
\[
 p_R+\partial_1\phi_4(r_3,r_4)=0\quad(h\ge4),\qquad
 p_R+\Pi'(r_3)=0\quad(h=3).
 \tag{7}
\]
These are the original stationary equations, including the full
complex marginals. No new supporting slopes are fitted.

At coordinate 3, the adjoining factor contributes the other
\(|d_N(X_3)|^{\beta/2}\). Multiplication restores the integer
power \(|d_N(X_3)|^\beta\). When \(m=4\), it is the complete
terminal transform that contributes this half, with
\(\Pi(z_3)=\mathcal P_{\epsilon_4}(z_3)-\beta g(z_3)/2\).
Thus no fourth ordinary vertex is required. At coordinates 1 and 2,
the full selected weights in (2) have already closed both incidences.
Every other retained diagonal weight is allocated exactly once
between its two adjacent factors.

Put \(I_m=\{j:6\le j\le m-5\}\), empty for \(m\le10\).
For type-compatible \(T\subseteq I_m\), set
\[
 S=\{1,2\}\cup T,\qquad
 \Im z_1=\Im z_2=1/100,\quad
 \Im z_j=7/500\ (j\in T),\quad
 \Im z_j=c_j\ (j\notin S),\qquad\mathbf x\in P^h.
 \tag{8}
\]
The incident ordinary factors of the safe interior selections are
\[
 E(T)=\{j\in\{2,\ldots,h\}:j-1\in T\text{ or }j\in T\}.
 \tag{9}
\]
Their indices are at least six, so they are disjoint from the cap
and factors 2 and 3 in (2). The
[interior-selection theorem](research_mixed_interior_selected_plateau.md)
applies to their actual inherited reference pairs and pays
\(1/200\) per incident factor, counting each factor once.
All other suffix factors use their completed unselected planes.
The terminal coordinate remains unselected.

The exact retained source for this selected set is
\[
 \mathscr J_{S,N}=U_{\epsilon_1,N}(w_L,X_1)
   \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
   \mathcal V_{\epsilon_m,N}(w_R,X_h)
   \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j}X_j^{-N\mathbf1_{j\in S}}.
 \tag{10}
\]
It retains the complete terminal private sum and terminal Fourier
alternatives. The exact outside scalar is still
\(\kappa_N^{m+k_4}N^{m+k_4-1}\), with \(|\kappa_N|=1\).

**Theorem 1.** For every fixed
word above and every \(\tau>0\),
\[
 |\mathscr J_{\{1,2\}\cup T,N}|
 \le C_{m,\tau}N^{A_{m,\tau}}
   \exp N\left\{M_{\rm open}-d_{12}
                  -\frac{|E(T)|}{200}+\tau\right\},
 \qquad M_{\rm open}=\Re\mathcal F_m(z_*).
 \tag{11}
\]
Both parities, small fixed ordinary-color disks, and fixed ordinary
jets on smaller disks are included.

*Proof.* Multiply (5) by the complete suffix and terminal bounds,
with exactly the allocations just described. Equations (6)--(7)
cancel the outgoing tangent. Every later internal complex tangent
cancels by the original stationary equation, also at the imaginary
displacements of the selected interior coordinates. Unused quadratic
remainders are nonpositive. For the fixed word choose the sum of
all source and color tolerances below \(\tau\). Cauchy's formula
is applied to the original integer-weighted holomorphic source on
smaller color disks; no modulus halfweight is differentiated.
This proves (11). \(\square\)

## 3. Combining first-only, second-only and simultaneous selections

Now permit any mixed first types and all type-compatible selections
\[
                         S\subseteq\{1,2\}\cup I_m.
 \tag{12}
\]
The compatibility condition is \(\epsilon_j=1\) whenever
\(j\in S\). Thus if the second type is three, position 2 cannot
occur in \(S\); if the first type is three, position 1 cannot occur.
The only new simultaneous case is exactly the one in Section 1.

Use the established contour for each exact selected summand:

- If \(S\cap\{1,2\}=\varnothing\), use the old interior contours.
- If \(S\cap\{1,2\}=\{1\}\), put the first height at \(7/625\)
  for next type three and at \(1/100\) for next type four.
- If \(S\cap\{1,2\}=\{2\}\), put the second height at \(1/100\).
- If \(S\supseteq\{1,2\}\), use (8).

Every selected safe interior coordinate has height \(7/500\), and
all other retained heights are original. Each exact Fourier summand
permits its own deformation in the full torus formula; this does not
identify plateau pieces at different heights. All these plateau
parametrizations have Jacobian one.

The [completed first-only theorem](research_mixed_first_selected_plateau.md)
has raw local gap \(1/2000\). The completed second-only theorems
have raw gaps \(1/400\) for first type three, and at least
\(1/3200\) for first type four; see respectively the
[first-three assembly](research_mixed_second_selected_first_three_plateau_completion.md)
and [first-four assembly](research_mixed_second_selected_plateau_completion.md).
Safe interior incidences have their unchanged gap \(1/200\).
Consequently one common raw local bound is
\[
             d_* =\min\{1/3200,d_{12}\}=1/3200.
 \tag{13}
\]
All nonempty selected sets in (12) therefore have a strict
finite-source gap \(d_*/2=1/6400\), after choosing the total
tolerance less than \(d_*/2\) and absorbing polynomial factors.
For sets containing neither boundary position, the larger interior
gap provides the same common bound. In particular, this conclusion
includes all four possibilities for the first two type flags. A
position whose flag is zero is simply not selectable.

## 4. The unchanged coefficient in the enlarged partial plateau sum

Let \(\mathcal Z_N^{\rm first\ two+int}\) be the sum of the plateau
integrals for all sets (12), including the empty set, multiplied by
the original outside scalar. All nonempty sets are exponentially
smaller than the unselected term. For a fixed
word there are finitely many sets, and the outside scalar has only
polynomial modulus. The original unselected packet therefore gives
\[
 \mathcal Z_N^{\rm first\ two+int}(-2,-2)
   =\kappa_N^{m+k_4}N^{-3/2}A_m
                 e^{N\mathcal F_m(z_*)}(1+O(N^{-1})),
 \qquad A_m\ne0.
 \tag{14}
\]
Its action, orientation, parity conventions, power and coefficient
are unchanged. On sufficiently small fixed ordinary-color disks the
same local packet and ordinary jets survive, by shrinking the disks
so that the moving original critical action changes by less than the
strict comparison reserve, followed by Cauchy's formula for the
exponentially small difference.

This is an expanded partial plateau integral. It does not claim an
asymptotic for the whole invariant. For \(m\ge11\), the retained
positions not in (12) are
\(\{3,4,5\}\cup\{m-4,m-3,m-2,m-1\}\), at most seven positions;
for \(4\le m\le10\) there are at most \(m-3\le7\).
Their selections, the nonplateau regions, whole-source boundary-color
estimates, short lengths and arbitrary short partial fillings remain
separate obligations for the cofinite filling-volume objective.
