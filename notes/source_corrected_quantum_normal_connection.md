# The actual source-corrected first quantum-normal connection

Independent construction and audit, 27 October 2026. The central freedom
in [the root regular profile](central_source_freedom_in_regular_profiles.md)
is removed by a first quantum-normal lifting rule when the selected
source has a nonzero kernel-to-cokernel symbol. The rule comes from
the same whole finite-sum preoperator. It does not assume horizontality
for the unsourced connection.

The nonzero-symbol hypothesis is essential and is not proved here for
every actual knot operator. The result is a constructive uniqueness
test for a specified source-normal comparison. It does not establish
the regulator comparison, selected growth, or a global profile.

## 1. The fixed whole input and the descended module

Use [the first-normal construction](first_quantum_normal_connection.md).
Fix \(Q=\zeta(1+\epsilon)\), \(\epsilon^2=0\), and put
\[
 E=\mathbb C(Y),\quad K_{\rm cent}=\mathbb C(U),\quad U=Y^N,
 \qquad \sigma_Q f(Y)=f(QY).
\]
Retain the specified whole Laurent Ore preoperator
\[
 \mathcal A(Q,Z,Y,S),\qquad P(Q,Y,S)=\mathcal A(Q,1,Y,S).
\]
The actual finite lift obeys
\(\mathcal A(Q,Q^N,Y,S_Q)G_N(Q,Y)=0\).
Assume the chosen root presentation
\(P=\sum_{j=0}^d a_jS^j\) has \(d\ge1\) and both
\(a_0(\zeta,Y),a_d(\zeta,Y)\ne0\) in \(E\). Fixed Laurent
shift normalizations are retained throughout.

Let \(A(Q,Y)\) be its solution companion:
\[
 \sigma_Q v=A v+e_d(Pf/a_d),\qquad
 v=(f,\sigma_Qf,\ldots,\sigma_Q^{d-1}f)^t,\qquad
 T=A^{-1}\sigma_Q .
\]
Write
\[
 L=T^N-I=L_0+\epsilon L_1,\quad
 \mathcal K=\ker L_0,\quad\mathcal C=\operatorname{coker}L_0,
 \quad \iota:\mathcal K\longrightarrow\mathcal C .
\]
The root \(T_0\) has order \(N\) on these two spaces.
Their invariants descend to \(K_{\rm cent}\), and
\[
 D_N:\mathcal K^{T_0}\longrightarrow\mathcal C^{T_0},
 \qquad D_N(v)=\pi L_1v/N^2
\]
has the already proved Leibniz rule
\[
 D_N(cv)=cD_N(v)+Uc'(U)\iota(v),\qquad c\in K_{\rm cent}. \tag{1}
\]

The first-coordinate map identifies \(\mathcal K^{T_0}\) with
the rational scalar solutions of \(P(\zeta,Y,S_\zeta)f=0\).
Indeed \(T_0v=v\) means \(\sigma_\zeta v=A_0v\); its first
\(d-1\) rows reconstruct all coordinates from the first, and
its last row is \(Pf=0\). Thus the source rule below depends
on the invariant vector, not on an arbitrarily chosen lift.

## 2. A linear source rule, rather than a fixed source value

For \(v\in\mathcal K^{T_0}\), let \(f\) be its first coordinate,
and define
\[
 h_1(v)=-N(\partial_Z\mathcal A)(\zeta,1,Y,S_\zeta)f,\qquad
 r_1(v)=A_0^{-1}e_d\,h_1(v)/a_d(\zeta,Y),                 \tag{2}
\]
\[
 R_N(v)=\frac1{N^2}\pi
                \sum_{j=0}^{N-1}T_0^jr_1(v).           \tag{3}
\]
Shifts outside the companion range in (2) are evaluated on
the reconstructed scalar solution. Equivalently reduce the
operator modulo the fixed root Laurent Ore operator \(P_0\).
Its two nonzero endpoint coefficients permit positive and
negative shifts; different remainders agree on the solution.

This is a well-defined \(K_{\rm cent}\)-linear map
\[
 R_N:\mathcal K^{T_0}\longrightarrow\mathcal C^{T_0}.     \tag{4}
\]
Every root shift fixes \(c(U)\), proving linearity of (2)
and (3). Its image is invariant since
\[
 T_0\sum_{j=0}^{N-1}T_0^jr_1-\sum_{j=0}^{N-1}T_0^jr_1
                =(T_0^N-I)r_1=L_0r_1,
\]
which vanishes in \(\mathcal C\). No rank-one assumption,
Jordan splitting, or inverse of \(\iota\) is used.

Define
\[
 \nabla_{\rm act}=D_N-R_N:
       \mathcal K^{T_0}\longrightarrow\mathcal C^{T_0}. \tag{5}
\]
It has symbol \(\iota\).

## 3. The same whole lift satisfies this corrected equation

Suppose \(f\) has a first-order lift \(G=f+\epsilon g\) obeying
the supplied equation
\(\mathcal A(Q,Q^N,Y,S_Q)G=O(\epsilon^2)\).
As \(Q^N=1+N\epsilon\),
\[
 P(Q,Y,S_Q)G=\epsilon h_1(v)+O(\epsilon^2).
\]
Its companion lift satisfies
\((T-I)v(Q)=\epsilon r_1(v)+O(\epsilon^2)\).
Apply the exact factorization
\[
 T^N-I=(I+T+\cdots+T^{N-1})(T-I)
\]
and project to \(\mathcal C\). This proves
\[
 D_N(v)=R_N(v),\qquad \nabla_{\rm act}(v)=0.             \tag{6}
\]
It does not assert \(D_N(v)=0\).

There is also an intrinsic first-order companion interpretation.
If \(\widetilde P(Q)=\mathcal A(Q,Q^N,Y,S)\) has the same
regular order as \(P\), then its companion perturbation gives
\[
 (\widetilde A_1-A_1)v=e_dh_1(v)/a_d,\qquad
 (\widetilde T_1-T_1)v=-r_1(v).
\]
Since \(T_0v=v\), differentiating its \(N\)-th power produces
exactly the negative average (3). Its kernel-to-cokernel
normal operator is therefore (5).

No common-order assumption is needed for the first-order result.
The literal whole order can increase through terms vanishing
at \(Z=1\). In the root Laurent Ore algebra reduce
\[
 N\partial_Z\mathcal A=J P_0+B,\qquad \deg B<d .
\]
Over dual numbers,
\[
 \widetilde P=(I+\epsilon J)[P(Q)+\epsilon B]
                       +O(\epsilon^2).
\]
The first factor is an Ore unit with inverse \(I-\epsilon J\).
Thus the effective regular rank-\(d\) companion has the same
first-order section problem and operator (5). This does not
assert such a fixed-rank reduction at all normal orders.

The construction is canonical relative to the supplied whole
preoperator and coherent source presentation. An arbitrary
\((Z-1)\)-change to \(\mathcal A\) changes the first-normal problem;
it is not a harmless replacement of the given input. Coherent
regular gauges of the same first-order section problem give the
usual canonical kernel/cokernel comparison.

## 4. Central uniqueness and the essential symbol hypothesis

Suppose both \(v\) and \(c(U)v\) admit the same whole first-order
lifting rule. By (1), (4), and (6),
\[
 0=\nabla_{\rm act}(cv)-c\nabla_{\rm act}(v)
                 =Uc'(U)\iota(v).                       \tag{7}
\]
If \(\iota(v)\ne0\) in the generic descended cokernel, then
\(c'=0\), so \(c\in\mathbb C\). A fixed nonzero ordinary-color
anchor sets that constant to one. Constancy required no
evaluation or regularity at the special central fiber \(U=1\).

Thus every nonconstant multiplier from
[the central profile freedom](central_source_freedom_in_regular_profiles.md)
is excluded by the same actual source-normal rule when this
hypothesis holds. A fixed source value for one section would
not suffice: the crucial input is the linear rule
\(R_N(cv)=cR_N(v)\) from the same whole preoperator.

A semisimple eigenvalue one of \(T_0^N\) makes \(\iota\) an
isomorphism, so every nonzero section satisfies the hypothesis.
The exact weaker condition is only \(\iota(v)\ne0\).
Neither condition has been established here for a general
knot's specified operator.

There is now a genuine all-knot witness in the canonical
[actual Mellin polarization](actual_mellin_normal_source_rigidity.md):
the observable quotient P^M Z/B supplies a dual monodromy row
with value one on the selected section. It proves selected-symbol
nonvanishing without either semisimplicity or a simple norm root.
It does not transfer that statement to a different meridian
regular-profile realization without its actual source map.

There is a directly checkable sufficient condition in the
intrinsic quantum-A norm polynomial. Let H_0=T_0^N and

    Delta_N(U,t)=det(tI-H_0).

Its coefficients descend to C(U). If

    partial_t Delta_N(U,1)!=0,

then eigenvalue one is simple over the generic central field,
so iota is an isomorphism there. Every nonzero actual root
section then satisfies the criterion. This uses the intrinsic
root norm of the specified quantum operator; it does not equate
Delta_N with the classical A-polynomial. A rank jump or collision
at U=1 does not by itself decide this generic condition; the
marked lattice is still required at that special fiber.

The condition cannot be dropped. Here is an exact algebraic
diagnostic, explicitly not a knot operator:
\[
 \mathcal A=(S-1)(S-Z),\qquad Z=Q^N,\qquad G_N=1+Y^N.
\]
The root operator is \(P=(S-1)^2\). Its companion monodromy
has a nontrivial Jordan block at one; its kernel lies in its
image, so \(\iota=0\) on the invariant solution line.
Moreover \(\partial_Z\mathcal A=1-S\) kills every root
central section, and \(\nabla_{\rm act}=0\) there.

For constants \(A,B\), the section \(A+B Y^N\) is another
exact lift for the SAME whole operator, with root ratio
\[
 c(U)=\frac{A+BU}{1+U}.
\]
When \(A+B=2\), all ordinary orbit values and the complete
value equal those of \(1+U\), yet this ratio can be nonconstant.
At second normal order the central equation begins with
\(N^2(U\partial_U)(U\partial_U-1)f\). This retains a
two-dimensional space until an additional pointing is supplied.
First-normal uniqueness is therefore a genuine symbol condition.

## 5. The actual factorial atom gives the claimed connection

For a finite quantum factorial used in the actual state,
\[
 G_N(Q,Y)=(Y;Q)_N,\qquad
 \mathcal A=S-\frac{1-ZY}{1-Y},
\]
the frozen operator is \(P=S-1\). Thus
\(D_N=U\partial_U\), \(\iota=1\), and
\(h_1(f)=-NYf/(1-Y)\). The elementary identity
\[
 \sum_{j=0}^{N-1}\frac{\zeta^jY}{1-\zeta^jY}
                     =\frac{NU}{1-U}
\]
gives
\[
 R_N(f)=-\frac{U}{1-U}f,\qquad
 \nabla_{\rm act}=U\partial_U+\frac{U}{1-U}.             \tag{8}
\]
Its rational horizontal sections are exactly \(C(1-U)\),
the actual root factorial and its constants. The unsourced
operator would wrongly exclude this section:
\(D_N(1-U)=-U\ne0\).

Equation (8) is an exact check from the finite-factorial atoms
of the actual state. It does not assume that the whole knot
state factors into such scalar horizontals. The theorem proves
a constructive restriction on pointed quantum comparisons;
it does not prove that candidate knot periods are scalar
multiples, that their compatible lift exists, or that their
selected geometric regulator norms coincide.

The [exact diagnostic script](../experiments/audit_source_corrected_quantum_normal_connection.py)
and [results](../experiments/source_corrected_quantum_normal_connection_results.json)
check the literal finite-factorial first-normal obstruction to
18 central rescalings, the seven Jordan symbol exceptions, and
15 hidden-higher-order reductions. Root arithmetic tests use
exact rational finite fields as convention checks; the proofs
above are in characteristic zero. The diagnostics do not assert
the nonzero symbol or simple norm root for a general knot.

