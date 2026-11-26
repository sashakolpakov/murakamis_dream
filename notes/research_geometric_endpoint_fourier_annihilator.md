# A fixed-width Fourier annihilator for the actual endpoint sector

Private written proof, 18 November 2026.

The boundary-propagation theorem P gives a fixed-order difference
equation for the actual source restricted to a fixed endpoint width.
Its classical symbol is a unit at the geometric clock pattern that
defined the restriction. Thus its formal local solution module there
is zero. The finite equation retains the full central normal
\(Q^N\); its root specialization must not replace that normal germ.

This is an auxiliary Fourier-source equation. It is not a minimal
peripheral knot equation, a comparison of relative cycles, or an
analytic bound for the original scalar. The sole complete proof
direct is P; the Fourier and formal-inverse arguments are given here.

## 1. The exact marked finite source and its shifts

Fix the separated geometric endpoint and expanded knot graph of P.
There are \(c\) crossings, \(d=N-1\), and the set \(I\) consists
of every wire or transfer edge whose geometric clock is one.
The cut clock is not one. Both row and column cases, and arbitrary
mixed lower/upper physical lifts, are included.

Use the primitive cut-and-transfer coordinates
\[
 k=(k_0,\ldots,k_c)\in\mathbb Z^{c+1},\qquad
                  a_e(k)=v_e\cdot k,\quad v_e\in\mathbb Z^{c+1}.
 \tag{1}
\]
The wire reconstruction is homogeneous and integral. Let \(S_N\)
be the original supported state set. Every wire and transfer
occupation lies between zero and \(d\).

Fix an integer \(B\ge0\), independent of \(N\), and assume
\[
                             (c+2)B<d.
 \tag{2}
\]
Retain the exact endpoint mask
\[
 \chi_{I,B,N}(k)
   =\prod_{i\in I}
       {\bf1}_{\{\min(a_i(k),d-a_i(k))\le B\}} .
 \tag{3}
\]
Let \(w_N(k;q,M,\mathbf m)\) be the literal source coefficient,
including its cut, pivots, framing, scalar factors and all retained
diagonal marks. More generally the argument permits arbitrary
complex coefficients on the same finite support. Define the entire
auxiliary Fourier function
\[
 \Psi_N(\xi;q,M,\mathbf m)
   =\sum_{k\in S_N}\chi_{I,B,N}(k)
       w_N(k;q,M,\mathbf m)\exp(\xi\cdot k),
       \qquad \xi\in\mathbb C^{c+1}.
 \tag{4}
\]
This definition inserts the actual mask; it does not discard
complementary source sectors or identify their periods.

Put \(Q=q^2=e^h\), using the actual local logarithm of \(Q\).
For each edge define the commuting shift
\[
              (\sigma_e f)(\xi)=f(\xi+h v_e).
 \tag{5}
\]
On an individual state exponential it acts by
\[
                    \sigma_e e^{\xi\cdot k}
                             =Q^{a_e(k)}e^{\xi\cdot k}.
 \tag{6}
\]
Linear relations between the \(v_e\)'s cause no problem: these
are the actual commuting translations, not independent fictitious
edge variables.

## 2. The central normal and exact annihilation

Introduce a central coefficient \(z\), and the fixed finite product
\[
 P_{I,B}(Q,z;\sigma)
   =\prod_{e\notin I}\prod_{t=0}^{B}
          (\sigma_e-Q^t)(\sigma_e-zQ^{-1-t}).
 \tag{7}
\]
Its number of factors is \(2(B+1)|E\setminus I|\), independent
of \(N\). Negative Laurent powers of \(Q\) are harmless since
\(Q\ne0\).

The full finite-source identity is
\[
 \boxed{\quad
       P_{I,B}(Q,Q^N;\sigma)\Psi_N=0 .
       \quad}
 \tag{8}
\]
It holds for every parameter value at which the retained coefficient
array is defined, before root specialization. In particular it
holds as a meromorphic identity if some chosen coefficient
presentation is meromorphic.

Indeed P's support theorem says that every state retained by (3)
has an edge \(e\notin I\) with
\[
                   a_e=t\quad\hbox{or}\quad a_e=d-t,
                              \qquad 0\le t\le B.
 \tag{9}
\]
In the first case the first factor in (7) kills that state.
In the second case
\[
                          Q^{a_e}=Q^{N-1-t}=Q^NQ^{-1-t},
 \tag{10}
\]
so the second factor kills it. Commutativity of the shifts proves
(8) term by term. No cancellation of amplitudes and no nonzero
coefficient assumption is used.

At the physical root \(h_N=2\pi i/N\), \(Q^N=1\), so (8) becomes
\[
                  P_{I,B}(Q,1;\sigma)\Psi_N=0.
 \tag{11}
\]
The upper endpoint is \(N-1-t\), not \(N-t\); its root eigenvalue
is exactly \(Q^{-1-t}\). Thus (11) retains the finite upper
offset even when \(B=0\).

The source coefficients in (4) may contain arbitrary retained
marks or depend on additional parameters. Those changes do not
affect the pointwise proof. An off-diagonal insertion or an affine
current that changes the support equations is a different array:
one must establish its support counterpart before applying (8).

## 3. Genuine normal derivatives

Equation (8), not (11), is the normal-germ identity. At fixed \(N\)
\[
                \partial_h Q^N=NQ^N.
 \tag{12}
\]
This contribution, and all its higher derivatives, remain in the
differentiated row. The source's \(M\)-dependence, scalar factors,
pivots and marks also remain in \(w_N\). No auxiliary pivot germ
is replaced by a different closed-source normal convention.

For example, writing \(P_N(h)=P_{I,B}(e^h,e^{Nh};\sigma(h))\),
ordinary differentiation gives the exact identity
\[
 \sum_{j=0}^{r}\binom rj
          (\partial_h^j P_N)(\partial_h^{r-j}\Psi_N)=0.
 \tag{13}
\]
Here differentiation of an operator includes its moving shifts.
For any translation \(T_v f(\xi)=f(\xi+h v)\),
\[
        \partial_h(T_v f)=T_v(\partial_h f+v\cdot\partial_\xi f).
 \tag{14}
\]
Equations (12)--(14) and the ordinary product rule give every
mixed quantum/meridian/mark normal row. They are finite identities;
they require no asymptotic regularity. On the ordinary color path
one restricts the entire identity to the actual prescribed
\(M(h)\), retaining its derivatives. Replacing \(Q^N\) by one
before differentiating would lose terms and is not allowed.

## 4. Formal local exclusion at the geometric clock covector

For the root-family formal row set \(Q=e^h\), \(z=1\), and expand
in the formal parameter \(h\). Its commutative principal symbol is
\[
          p_0(\lambda)
             =\prod_{e\notin I}(\lambda_e-1)^{2(B+1)}.
 \tag{15}
\]
Let \(\xi_*\) be a local Fourier base point and let
\(W(\xi)\) be a holomorphic phase germ. The shift eigenvalues
associated to its covector are
\[
                      \lambda_e(\xi)
                         =\exp(v_e\cdot\partial_\xi W(\xi)).
 \tag{16}
\]
If these equal the specified geometric clocks at \(\xi_*\), then
every \(\lambda_e(\xi_*)\ne1\) for \(e\notin I\), by the
definition of \(I\). Hence
\[
                         p_0(\lambda(\xi_*))\ne0.
 \tag{17}
\]
The same conclusion holds for any phase with these nonunit
inequalities, without requiring a geometric interpretation.

Here is an explicit formal inverse. On holomorphic germs in \(\xi\),
conjugation of one shift gives
\[
 e^{-W/h}\sigma_e e^{W/h}A
   =\exp\!\left(\frac{W(\xi+h v_e)-W(\xi)}h\right)
                  A(\xi+h v_e).
 \tag{18}
\]
Taylor expansion is a well-defined formal differential operator:
at every power of \(h\) it uses finitely many derivatives.
Conjugating the finite product (11) therefore gives
\[
 L_W=e^{-W/h}P_{I,B}(e^h,1;\sigma)e^{W/h}
       =p_0(\lambda(\xi))+\sum_{\ell\ge1}h^\ell L_\ell,
 \tag{19}
\]
where each \(L_\ell\) has holomorphic coefficients and finite
differential order. Shrink the germ so that the first coefficient
is a unit. For a prescribed formal right side
\(F=\sum_{n\ge0}h^nF_n\), solve \(L_W A=F\) recursively by
\[
 \begin{split}
 A_0&=p_0^{-1}F_0,\\
 A_n&=p_0^{-1}
      \left(F_n-\sum_{\ell=1}^{n}L_\ell A_{n-\ell}\right).
 \end{split}
 \tag{20}
\]
Thus the conjugated formal operator is bijective on
holomorphic-germ power series. In particular its kernel is zero.
The same argument applies after a fixed Laurent or fractional
power prefactor in \(h\), since the shifts act only in \(\xi\).

Consequently a formal WKB expression \(e^{W/h}A\) satisfying
the row (11) at this clock covector has \(A=0\). This is a local
statement about formal solutions of the exact auxiliary equation.
For an asserted asymptotic decomposition of the actual sequence,
one must still justify that the row acts on its components, or
supply a shift-stable expansion to which (18)--(20) apply.
The finite root identities alone do not define such a decomposition.

## 5. Scope of the reduction

Equations (8) and (15)--(20) turn the support obstruction into a
fixed-order quantum difference row and a formal local exclusion.
They do not identify an annihilator of the unrestricted source,
delete the mask (3), or identify this row with the peripheral
\(A\)-polynomial. No minimality or automatic pushforward of a
geometric factor is asserted.

For widths \(B_N=o(N)\), P still gives the support statement and
the same pointwise product with \(B=B_N\). Its order now grows.
Its endpoint eigenvalues approach one, but the fixed-order formal
inverse proof gives no uniform analytic bound for this family.
Even for fixed \(B\), no bounds for the coefficients in (20),
no analytic parametrix and no scalar exponential estimate are
claimed.

All complementary endpoint sectors, factorial continuations,
Fourier aliases and relative interface currents remain to be
compared with the original cycle. In particular a root specialization
or a formal unit cannot replace that comparison by a nonzero
geometric period.

## Complete proof-source pin

* P: notes/research_geometric_endpoint_boundary_propagation.md,
  SHA256 cda3efe3cf89267f9a3a351e1ad0d2a07f09c24ea3d10ee45fbb1d9ea11bb3c0.

The complete source was freshly read nontruncated in this author
sequence; every used support and coordinate implication was checked.
All additional arguments are proved inline. Only private written
mathematics and text/hash operations were used.
