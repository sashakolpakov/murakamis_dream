# Adjacent short fillings: the exact charge class and the remaining contour problem

Research note, 3 November 2026.

An arbitrary rational word already has an exact finite integral in the
original source algebra. The missing step is a bound for its coherent
integrand, together with a nonzero contribution from the geometric
critical point. This note identifies one cancellation invariant of that
integral. It is preserved with arbitrary attached sources and retains
the full root multiplicities. It removes no short-turn obstruction by
itself.

The exact representations used here are
[the arbitrary-power compiler](research_arbitrary_power_source_compilation.md),
[internal-wire averaging](research_internal_wire_exact_circle_averaging.md),
and [the polynomial-crossing Fourier trace](research_polynomial_crossing_fourier_trace.md).
The new calculation is the finite charge difference and its Green
inverse in Sections 2--3. Section 5 states an unproved general contour
criterion, not a new asymptotic theorem.

## 1. The original connected source and its finite charge vectors

Put \(D=N-1\), \(\eta=(-1)^D\), and
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f .
 \tag{1}
\]
Here \(T_N\) is the ordinary Chebyshev polynomial. The double roots
retain their first derivatives; the odd-level simple root retains its
value. Let
\[
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u).
 \tag{2}
\]

For a fixed connected selected subtree \(C\), give each boundary
incidence its own variable \(u_e\). Its exact source is
\[
 Z_{C,N}(\mathbf u)=
 \left(\prod_{v\in C}\phi_N^{(t_v)}\right)
 \left[
 \prod_{v\in C}R(t_v)^{n_v}
 \prod_{vw\in E(C)}K_N(t_v,t_w)
 \prod_{e=(v,\partial C)}K_N(t_v,u_e)
 \right].
 \tag{3}
\]
Every \(n_v\) is a fixed signed integer. The powers in (3) are algebra
powers, including negative powers. At a free variable the entire
ordinary polynomial is retained. Boundary variables may be identified
after this identity; their resulting higher-degree products must then
remain. A rational pendant word is the path case of (3), and a rational
piece with both ends exposed is the path with two boundary incidences.
Identity rather than turn connections use the exact identity kernel
from the compiler; the argument below is unchanged.

Replace each \(R^{n_v}\) by its canonical degree-\(D\) polynomial.
The expression in square brackets is then a separately even
trigonometric polynomial \(Q_N(\mathbf t;\mathbf u)\). At a vertex of
original degree \(d_v\), its Fourier degree is at most
\((d_v+1)D\). Write
\[
 Q_N=\sum_{\mathbf k}a_{\mathbf k}(\mathbf u)
                         e^{i\mathbf k\cdot\mathbf t}.
 \tag{4}
\]
For a positive charge vector \(\boldsymbol\ell\), define
\[
 d_{\boldsymbol\ell}=
 \sum_{\boldsymbol\varepsilon\in\{-1,1\}^{C}}
 \left(\prod_{v\in C}-\varepsilon_v\right)
 a_{\,N\boldsymbol\ell+\boldsymbol\varepsilon},
 \qquad
 g_{\boldsymbol\ell}=\eta^{\sum_v\ell_v}d_{\boldsymbol\ell}.
 \tag{5}
\]
Coefficients outside the actual Fourier support are zero. Iterating the
original derivative-sampling trace gives exactly
\[
 \boxed{\displaystyle
 Z_{C,N}=N^{2|C|}\eta^{|C|}
       \sum_{\boldsymbol\ell\ge\mathbf1}
        \left(\prod_v\ell_v\right)g_{\boldsymbol\ell}.}
 \tag{6}
\]
This is an identity of the whole free-boundary polynomial. If
\(N>\max_v d_v\), only \(1\le\ell_v\le d_v\) can occur. In particular
an internal vertex of a rational path has at most two charges, regardless
of the size of its fixed crossing power.

Each charge in (6) is also an exact integral over a product of complete
angular periods. The polynomial integrand is entire and periodic, so
those complete periods have no vertical endpoint current. Alternatively
one may use the canonical factorial factors and the exact meromorphic
trace kernel. In that representation the Gaussian crossing interpolation
is valid at the physical jets, but every resulting endpoint current must
be retained. These are two representations of (3), not two different
sources.

## 2. A change by the physical relation is a charge second difference

The physical relation has the exact angular expression
\[
 P_N(-2\cos t)=2-\eta(e^{iNt}+e^{-iNt}).
 \tag{7}
\]
Let \(h(t)\) be an even trigonometric polynomial, with coefficients in
any vector space of spectator boundary polynomials. For every integer
\(\ell\), put
\[
 d_\ell(h)=\widehat h_{\ell N-1}-\widehat h_{\ell N+1},
 \qquad b_\ell=\eta^\ell d_\ell(h).
 \tag{8}
\]
Evenness gives \(b_0=0\) and \(b_{-\ell}=-b_\ell\). Direct coefficient
multiplication in (7) proves
\[
 \eta^\ell d_\ell(P_Nh)
     =2b_\ell-b_{\ell-1}-b_{\ell+1}.
 \tag{9}
\]
Thus the change is the Dirichlet second difference on the positive
charge half-line. Its weighted first moment vanishes:
\[
 \sum_{\ell\ge1}\ell
       (2b_\ell-b_{\ell-1}-b_{\ell+1})=0.
 \tag{10}
\]
All sums are finite. Equation (10) follows by shifting the two sums;
the sole lower boundary value is \(b_0=0\).

In a network, a modification \(Q_N\mapsto Q_N+P_N(t_v)h_N\)
has exactly (9) in coordinate \(v\), and hence leaves (6) unchanged.
Multiplying by any original crossing coupon, incident kernel or
attached finite source preserves this statement: the difference is
still divisible by \(P_N(t_v)\) before the full trace is taken.
The argument includes the mixed first normals when other variables
also lie at double roots. It is stronger than agreement merely at
the distinct spectral values.

This invariance is confined to contracted variables. At an untraced
boundary, adding \(P_N(u)h(u)\) changes the ordinary boundary
polynomial, and is not an allowed replacement in a whole-boundary
packet theorem.

## 3. The complete finite charge reduction has no level-dependent cost

Let \(g=(g_1,\ldots,g_L)\) be a finite charge sequence. Define its
moment and its projection onto charge one by
\[
 m(g)=\sum_{j=1}^{L}j g_j,\qquad
 (\Pi g)_\ell=\mathbf1_{\ell=1}m(g).
 \tag{11}
\]
For a zero-moment sequence \(q\), define
\[
 (\mathcal Gq)_\ell=\sum_{j=1}^{L}\min(\ell,j)q_j,
 \qquad \ell\ge0.
 \tag{12}
\]
Then \((\mathcal Gq)_0=0\), and
\((\mathcal Gq)_\ell=m(q)=0\) for \(\ell\ge L\).
Since
\[
 2\min(\ell,j)-\min(\ell-1,j)-\min(\ell+1,j)
                       =\mathbf1_{\ell=j},
 \tag{13}
\]
the finite sequence (12) solves
\[
          \Delta_D\mathcal Gq=q,\qquad
          (\Delta_Db)_\ell=2b_\ell-b_{\ell-1}-b_{\ell+1}.
 \tag{14}
\]
Conversely (10) shows that every finite Dirichlet second difference
has zero moment. Thus the quotient of finite charge sequences by
these differences is exactly one dimensional, represented by the
weighted moment (11).

For coefficients with any norm,
\[
 \|\Pi g\|_1\le L\|g\|_1,\qquad
 \|\mathcal Gq\|_1\le L^2\|q\|_1.
 \tag{15}
\]
The second bound follows by summing
\(\min(\ell,j)\le L\) over the at most \(L\) nonzero rows.
These constants depend on the charge range, not on the quantum level.

For several vertices, apply \(\Pi_v\) in each coordinate. The
telescoping identity
\[
 g-\Pi_1\cdots\Pi_mg
 =\sum_{v=1}^{m}\Pi_1\cdots\Pi_{v-1}(I-\Pi_v)g
 \tag{16}
\]
and (12) express the left side as a sum of coordinate Dirichlet
second differences. Its sole surviving entry is
\[
 (\Pi_1\cdots\Pi_mg)_{(1,\ldots,1)}
             =\sum_{\boldsymbol\ell}
                    \left(\prod_v\ell_v\right)g_{\boldsymbol\ell}.
 \tag{17}
\]
For a fixed network the operator bounds obtained from (15) are
independent of \(N\). This gives an exact, finite way of grouping all
cancellation between charge vectors, with arbitrary free-boundary
coefficients.

This statement is about the charge arrays, after Fourier coefficient
extraction. It does not say that their Green primitives are small
pointwise on a proposed deformed angle cycle, nor identify their
images with geometrically admissible source interpolations. In
particular it does not manufacture a favorable saddle contour.

## 4. Why this does not settle a short turn

The only surviving charge in the terminal source
\[
                    \phi_N[R^2K_N(t,0)]
 \tag{18}
\]
already contains cancellation at a strictly larger exponential rate.
The canonical crossing coefficient at Fourier frequency \(N-1\) is
\(1/N\). Its individual contribution to that charge is
\[
 \pi N^{-2}e^{NM_\infty}(1+O(N^{-1})),
 \tag{19}
\]
whereas the whole original terminal has real rate \(M_\infty/2\).
Both statements, with their exact scalar and both level parities, are
proved in Section 5 of the polynomial-crossing Fourier note.
There is no second charge available to cancel (19). The cancellation
is between crossing Fourier modes inside the one charge.

Consequently (12)--(17) resolve the algebra of inter-charge
cancellation but provide no estimate for the coherent coefficient
left in (17). Taking absolute values of its crossing-mode summands
would already fail on the proved hyperbolic terminal (18).

There is also no invariant class consisting only of concentrated
boundary packets that is closed under all turns:
\[
                  H_p=T(R^p),\qquad T(H_p)=R^p.
 \tag{20}
\]
For \(|p|\ge2\) the first is a proved concentrated packet; the second
has unit-modulus values at every physical angle. Any proposed
composition condition must retain information about the actual word
and its attached cycle that distinguishes these cases. Its exact
classical canonical graph or a nonzero finite coefficient vector alone
does not supply that information.

## 5. A precise remaining theorem, still unproved

For a connected short component, the required theorem would concern
the exact polynomial (3), not a product of independently chosen local
saddle contributions. Its analytic conclusion should supply:

1. A holomorphic nonzero full-boundary expansion on one fixed
   neighborhood of the complete boundary values, with the original
   carriers and all level parities retained.
2. A strict exponential loss on the rest of the whole real boundary,
   and a complex-strip bound strong enough to apply the original
   derivative traces after attaching arbitrary already-controlled
   pieces.
3. The actual marked primitive periods of that component and an
   absolute real-action anchor. A formal solution of the gluing
   equations is insufficient for this identification.

For a tree component with \(b\) independent boundary incidences the
expected power is \(N^{-3(b-1)/2}\), as in every proved block.
On a regular edge chart this normalization follows from \(m\)
vertex traces, \(m+b-1\) edge packets and \(m\) angle Gaussians:
\[
 2m-\frac32(m+b-1)-\frac m2=-\frac32(b-1).
 \tag{21}
\]
If that chart folds, a replacement Newton-coordinate calculation must
establish the same normalization; equation (21) alone does not do so.

A sufficient contour criterion can be stated without assigning
positive weights to the Fourier charges. In the exact restored
angle/wire representation, deform the full original cycle, including
every residue or endpoint current created in the deformation, into
a selected critical neighborhood and a remainder. Require:

* a holomorphic nondegenerate critical phase whose local density,
  lattice normalization and complete original carrier are known;
* a nonzero coefficient of that critical contribution for the actual
  source cycle, after grouping all contributions with its action,
  at both parities;
* an absolute integral bound below its real action by a fixed positive
  amount for the grouped remainder, uniformly in the boundary
  neighborhood, plus the whole real-boundary loss above.

Ordinary holomorphic stationary phase then gives the desired local
expansion; the remainder estimate makes it a theorem for the whole
source. On a regular edge chart the first-charge phase is
\[
 \sum_{vw\in E(C)}\psi(t_v,t_w)
 +\sum_{e=(v,\partial C)}\psi(t_v,u_e)
 +\sum_{v\in C}\left(\frac{in_vt_v^2}{4\pi}-it_v\right).
 \tag{22}
\]
Neither (22) nor its Hessian is asserted through an edge fold.
The exact Newton or restored-trace representation must be used there.

The two unresolved requirements are therefore concrete: construct the
needed joint cycle for arbitrary adjacent short words, and prove that
its geometric contribution survives the coherent crossing sums.
The exact charge class (6), its relation (9), and internal-wire
averaging are stable under arbitrary source attachment. They can
organize such a proof, but the size and nonvanishing requirements in
this section have not been established in general.
