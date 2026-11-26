# A bounded source order for every partially contracted tree

Private written deduction, 13 November 2026. This note proves an
unconditional algebraic statement for every fixed partially filled
circle tree, with arbitrary signed powers and its full ordinary free
boundary polynomial. It gives a nonzero moment after a bounded number
of derivatives in the existing auxiliary scalar smoothing. The bound
depends on the filled vertices and their degrees, and is independent
of the level and the magnitudes of the fixed powers.

This smoothing is not identified with the physical meridian deformation
or with an action-normalized geometric critical component. The theorem
does not give a nonzero geometric coefficient or a Kashaev volume limit.
Its addition to the existing generic residue nonvanishing result is
that nonvanishing persists after all internal tree contractions, with
a bounded order at the physical fiber for the entire free polynomial.

## 1. The exact auxiliary family

Fix a finite tree \(T=(V,E)\), a nonempty set \(U\subset V\) of
unfilled vertices, and its complement \(S=V\setminus U\). At every
\(v\in S\), fix an arbitrary integer power \(n_v\). At level
\(N\ge2\), let \(D=N-1\), and retain the original objects
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \mathcal A_0=\mathbb C[z]/(P_N),\qquad
 \phi_0(e_i e_j)=\delta_{i+j,D},\qquad
 \mathsf T e_i=e_{D-i}.
 \tag{1}
\]
The \(e_i\) are the original Newton polynomials, of degree \(i\).
Write
\[
 K_T(z,w)=\sum_{i=0}^{D}e_i(z)e_i(w).
 \tag{2}
\]
For each fixed integer \(n\), let \(C_{n,N}(z)\) be the canonical
degree-less-than-\(N\) polynomial representing the actual crossing
power \(R^n\) in \(\mathcal A_0\). It is nonzero, including when
\(n\) is negative, because \(R^n\) is a unit in the original algebra.

Use the common auxiliary parameter \(s\) and the exact family
\[
 \mathcal A_s=\mathbb C[s,z]/(P_N(z)-s),\qquad
 \phi_s(f)=(-1)^D N^2[z^D]\operatorname{rem}_{P_N-s}f.
 \tag{3}
\]
Keep \(C_{n,N}\) fixed as a polynomial throughout this family. In
particular \(C_{-1,N}\) and \(C_{1,N}^{-1}\) need not be the same
section away from \(s=0\). The family is attached to the recorded
physical expression and is exact at its physical fiber; it asserts no
off-fiber inverse or isotopy identity.

The [dualizing-residue construction](research_actual_source_dualizing_residue.md),
Section 3, proves
\[
 \phi_s(e_i e_j)=\delta_{i+j,D},\qquad
 \phi_{s,w}(K_T(z,w)f(w))=(\mathsf T f)(z).
 \tag{4}
\]
Thus the original turn remains an invertible, constant matrix in
Newton coordinates at every \(s\).

Define the ordinary polynomial in the free variables
\(\mathbf z_U=(z_u)_{u\in U}\) by
\[
 F_N(s;\mathbf z_U)=
 \left(\prod_{v\in S}\phi_{s,z_v}\right)
 \left\{
    \prod_{v\in S} C_{n_v,N}(z_v)
    \prod_{\{v,w\}\in E}K_T(z_v,z_w)
 \right\}.
 \tag{5}
\]
Each trace in (5) acts only on its own variable. No reduction is made
in any free variable. Equation (5) specializes at \(s=0\) to the
original partially filled tree source, including its first physical
normal data at every contracted vertex. Any original nonzero framing
scalar can be retained as an external factor throughout.

## 2. The bounded-order theorem

Put
\[
                   B(T,S)=\sum_{v\in S}(\deg_T(v)-1).
 \tag{6}
\]
This integer is nonnegative: because \(U\ne\varnothing\), every
filled vertex has degree at least one.

**Theorem.** At every level \(N\ge2\), the polynomial (5) is nonzero
and satisfies
\[
 \deg_s F_N\le B(T,S),\qquad
 \deg_{z_u}F_N\le D\deg_T(u)\quad(u\in U).
 \tag{7}
\]
Consequently there is an integer \(r_N\) with
\[
 0\le r_N\le B(T,S),\qquad
 \partial_s^{r_N}F_N(0;\mathbf z_U)\ne0.
 \tag{8}
\]
The conclusion is a polynomial identity in all free variables. It
does not discard high ordinary degrees at those variables.

**Proof of the degree bound.** Work over any coefficient ring
containing the remaining variables. If \(f,g\) have degree below
\(N\) in \(z\), divide their product first by \(P_N\):
\[
                  fg=qP_N+r,
       \qquad \deg_zq\le N-2,\quad \deg_zr<N.
\]
Then
\[
          \operatorname{rem}_{P_N-s}(fg)=r+s q.
 \tag{9}
\]
Polynomial division by the fixed monic \(P_N\) introduces no new
\(s\)-degrees into \(q,r\). Thus one multiplication of two
canonical representatives increases the sum of their \(s\)-degrees
by at most one. The original turn in (4) does not increase that
degree.

Root the tree at any \(u_0\in U\). A filled vertex \(v\), with
children \(v_1,\ldots,v_c\), sends towards its parent the canonical
ordinary polynomial
\[
 \mathsf T\left(
     C_{n_v,N}\prod_{j=1}^{c}H_{v_j}\right),
 \tag{10}
\]
where the product inside the turn is taken in \(\mathcal A_s\),
and the output coordinate is the parent coordinate. Formula (10)
is precisely its original trace against (2), by (4). There are
\(c\) multiplications after the coupon is inserted, so this node
adds at most \(c=\deg_T(v)-1\) to the sum of the child bounds.

An unfilled nonroot vertex \(v\) instead sends
\[
 K_T(z_v,z_{\mathrm{parent}})
                  \prod_{j=1}^{c}H_{v_j}(z_v).
 \tag{11}
\]
There is no quotient or trace in \(z_v\), and (11) adds no
\(s\)-degree. At the unfilled root, take just the ordinary product
of its incoming messages. Adding these bounds proves the first
inequality in (7). Each original edge contributes degree at most
\(D\) in either incident free variable; the contractions in other
variables do not increase those degrees. This proves the second
inequality.

**Proof of nonvanishing.** Let \(L\) be the rational function field
in all the free variables other than the current output variable,
with any fixed level constants adjoined. The algebra
\[
                   K=L(s)[z]/(P_N(z)-s)
 \tag{12}
\]
is a field. Indeed
\(L[s,z]/(P_N(z)-s)\simeq L[z]\) is a domain, free of rank \(N\)
over \(L[s]\). Its localization over \(L(s)\) is a
finite-dimensional domain over a field, hence is itself a field.

In this field every frozen coupon \(C_{n,N}\) is nonzero because
its degree is below \(N\). The turn is an invertible linear map
over \(L(s)\), by (4). Therefore (10) is nonzero whenever all its
child messages are nonzero in (12).

Every message reaching a filled vertex has degree below \(N\) in
that vertex's coordinate. A nonzero such polynomial stays nonzero
in (12). For an unfilled vertex, its incoming messages are nonzero
ordinary polynomials in its independent free coordinate. Their
ordinary product is nonzero. The factor \(K_T\) in (11) is nonzero
as a polynomial in the parent coordinate: the Newton expansion (2)
has among its coefficients \(e_0(z_v)=1\). Thus (11) is also nonzero.
Induction from the leaves proves that all messages are nonzero, and
the ordinary product at the unfilled root is nonzero. This proves
nonvanishing in (7). A nonzero polynomial in \(s\) of degree at
most \(B(T,S)\) has a nonzero coefficient of order at most that
integer. In characteristic zero this is equivalent to (8). QED.

## 3. Exact moment interpretation

For an open canonical message write
\[
            H_N(s,z)=\sum_{i=0}^{D}a_{i,N}(s)e_i(z).
\]
Its original dual Newton observations satisfy exactly
\[
          \phi_s(e_{D-i}H_N)=a_{i,N}(s).
 \tag{13}
\]
The proof above says that the full moment vector in (13) is nonzero
after all contractions below that output, and its entries have the
specified bounded \(s\)-degree. At least one of their derivatives
through that degree is nonzero at zero. No division by an unknown
closed invariant is used to obtain these moments.

For the generic field (12), the residue density of this message is
\(H_N/P_N'\), up to the retained scalar in (3). It is nonzero,
and therefore has nonzero value under every generic embedding of
(12). This conclusion now concerns the internally contracted open
message, as distinct from the uncontracted product numerator of a
multivariable residue formula.

There is also a direct moment certificate for the entire unreduced
polynomial (5). Choose any \(u_0\in U\), and set
\[
 m_{i,N}(s;\mathbf z_{U\setminus\{u_0\}})
   =\phi_{s,z_{u_0}}
         \bigl(e_{D-i}(z_{u_0})F_N(s;\mathbf z_U)\bigr),
 \qquad 0\le i<N.
 \tag{14}
\]
Then the vector in (14) is nonzero and every entry has \(s\)-degree
at most
\[
          B(T,S)+\max\{\deg_T(u_0)-1,0\}.
 \tag{15}
\]
Indeed the root output is a product of \(\deg_T(u_0)\) incoming
canonical messages. Each is nonzero in the generic field (12),
so their product remains nonzero after reduction there. Reducing
that product adds at most \(\deg_T(u_0)-1\) to its \(s\)-degree
when the degree is positive; an isolated unfilled root has output
one. Formula (13) then identifies (14) with the resulting Newton
coefficient vector. At least one of these exact inserted observations
therefore has a nonzero derivative at zero of order at most (15).
The insertion and trace in (14) are specified explicitly; this is
not an assertion that the originally prescribed eventual filling
row has a nonzero component.

## 4. What the bounded order does not establish

The integer in (8) may be positive. Products in the physical algebra
can vanish because that algebra has nilpotents, although the generic
field product cannot. The theorem retains this possibility rather
than asserting a nonzero physical zeroth jet. A final scalar trace
can also annihilate a nonzero message: already
\(\phi_s(1)=0\) for \(N\ge2\). This is why a free boundary, or the
full vector of moments (13), is retained in the conclusion.

The derivatives in (8) belong to the specified auxiliary family with
frozen crossing polynomials. They are not the original meridian
derivatives unless a further comparison proves that identification.
Likewise the field (12) has degree \(N\), and its branches are
spectral branches of the finite pair algebra. They have not been
identified with the fixed geometric critical field. The moment vector
has \(N\) entries; its nonzero entry and derivative order may depend
on \(N\). It is not a fixed finite-dimensional whole critical-source
descent. Neither this nonvanishing nor the bounded jet order gives a lower bound for the
prescribed geometric coefficient as \(N\) grows.

Thus this theorem supplies a finite-order source certificate for
every partially contracted tree, without selecting a list of short
blocks. A use in the original volume problem still needs a
source-preserving comparison of this finite source with the geometric
period, preserving the physical zeroth observation and its action.
The bounded auxiliary order does not replace that comparison.

No numerical mathematical computation, test, import, compilation,
manuscript edit, public-document edit, or frozen-proof edit is used.
