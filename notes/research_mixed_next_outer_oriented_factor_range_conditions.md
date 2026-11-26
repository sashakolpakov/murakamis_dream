# Range conditions after the first oriented symbol-root crossing

Private exact-source deduction, 9 November 2026. A directional factor
of the original symbol has a larger outward zero-free width near the
half-frequency endpoint. Passing the first zero of the other factor,
however, changes the frozen half-line range. The resulting condition is
an explicit linear compatibility, with the Toeplitz factor order and
the boundary defect of the two-factor product retained.

A separate finite-source argument proves that the complete outgoing
polynomial family spans its entire polynomial target space. Thus a
fixed proper range cannot contain that family on an open output domain,
even after a fixed surjective compression. This does not decide a
parameter-dependent construction or the signed observation. No
mathematical numerical evaluation, saved-value arithmetic, or
frozen-source edit is used.

## 1. The original oriented factors

Use the exact degree-eleven polynomials
\(\mathscr F_\pm(z,w)\) from
[the factorization theorem](research_mixed_next_outer_degree_eleven_factors.md).
Here \(z=e^{iu}\), \(w=e^{i\pi t}\), and \(0\le t<1/2\).
The symbol variable \(z\) is independent of the outgoing parameter
\(Z\) used in Section 5. Set
\[
 a_+(z,t)=w^{-3}z^{-6}\mathscr F_+(z,w),\qquad
 a_-(z,t)=w^{-3}z^{-5}\mathscr F_-(z,w).
 \tag{1}
\]
Their exact Laurent bands are, respectively, \([-6,5]\) and
\([-5,6]\). All four extreme coefficients are nonzero. The
original full symbol satisfies
\[
 p(z,t)=a_+(z,t)a_-(z,t),\qquad
 a_-(e^{iu},t)=\overline{a_+(e^{iu},t)}
 \quad(u,t\ \text{real}).
 \tag{2}
\]
The six/five inside-root counts of that source give winding zero
for each factor on the unit circle.

For completeness, write \(x=u/2\) and let \(F(x,\pi t)\) be the
real entire trigonometric function in the same factorization.
Then
\[
 a_\pm(e^{iu},t)
   =16e^{\mp ix}\{F(x,\pi t)\pm i\sin^3x\}.
 \tag{3}
\]
The identity \(F(-x,-\theta)=F(x,\theta)\) proves
\[
                         a_+(-u,-t)=a_-(u,t).
 \tag{4}
\]
Here the factors are written as angular functions in (4).
In particular, the original simultaneous reflection exchanges the
factors. Neither factor separately inherits the even-space closure
of the original full symbol.

There is a fixed left neighborhood of \(t=1/2\) on which the first
outward crossing of the full symbol is a unique simple zero of
\(a_-\). Indeed the
[endpoint-root theorem](research_mixed_next_outer_symbol_endpoint_roots.md)
gives the three endpoint roots of \(\mathscr F_+\) from
\[
 c_0=-\frac12,\qquad
 c_\pm=\frac{1+2i\pm\sqrt{5-4i}}4,\qquad
 u_c=\frac{2\pi}{3+ic}(1/2-t)+O((1/2-t)^3).
 \tag{5}
\]
The \(c_0,c_-\) branches are inside the unit circle and the
selected \(c_+\) branch is outside. Their reciprocal conjugates
are the roots of \(\mathscr F_-\). The \(c_0\) slope is strictly
the smallest of all six slopes, and all other sixteen full-symbol
roots remain separated from the circle. Thus, for each fixed
\(t\) sufficiently close to \(1/2\), let \(h_1(t)\) be the first
positive log modulus of an outer zero and let \(h_2(t)>h_1(t)\)
be the next distinct outer log modulus. For any
\[
                         h_1(t)<\lambda<h_2(t),
 \tag{6}
\]
the shifted Laurent symbols
\[
 A(z)=a_+(e^\lambda z,t),\qquad
 B(z)=a_-(e^\lambda z,t),\qquad
 P(z)=p(e^\lambda z,t)=A(z)B(z)
 \tag{7}
\]
are nonzero on the unit circle and have windings \(0,1,1\),
respectively. This conclusion uses exactly one simple crossing.
It makes no assertion about the number of crossings at a larger
height below the selected geometric root.

## 2. Exact half-line range and solution

Let \(H=\ell^2(\mathbb N_0)\). For a Laurent polynomial
\(b(z)=\sum b_jz^j\), use
\[
 (T(b)f)_n=\sum_{k\ge0}b_{n-k}f_k,\qquad
 S=T(z),\quad (Sf)_0=0,\quad(Sf)_n=f_{n-1}\ (n\ge1).
 \tag{8}
\]
Fix a symbol \(B\) as in (7). Its pole order at zero is five,
and it has six roots inside and five outside the unit circle,
counting multiplicities. Consequently it has the exact canonical
factorization
\[
 B(z)=c\,b_-(z)\,z\,b_+(z),\qquad c\ne0,
 \tag{9}
\]
where
\[
 b_-(z)=\prod_{|\rho_j|<1}(1-\rho_j/z),\qquad
 b_+(z)=\prod_{|\rho_j|>1}(1-z/\rho_j).
 \tag{10}
\]
The roots are those of the shifted polynomial \(z^5B(z)\).
None is zero. The subscript on \(b_-\) denotes its nonpositive
Laurent powers and is distinct from the oriented factor \(a_-\).

The factors and their inverses have absolutely summable Laurent
series, respectively of nonpositive and nonnegative degree.
The exact Toeplitz order is
\[
 T(B)=c\,T(b_-)S\,T(b_+).
 \tag{11}
\]
To check it, a nonpositive power followed by a nonnegative power
obeys \((S^*)^rS^s=T(z^{s-r})\); expand the absolutely convergent
series in that order. The two outer operators in (11) are bounded
and invertible, with inverses \(T(b_-^{-1})\) and \(T(b_+^{-1})\).

**Half-line range theorem.** The operator \(T(B)\) is injective,
has closed range of codimension one, and
\[
 \boxed{\quad
 (\exists v\in H:\ T(B)v=f)\ \Longleftrightarrow\
 [T(b_-^{-1})f]_0=0 .
 \quad}
 \tag{12}
\]
When (12) holds, its unique solution is
\[
 v=c^{-1}T(b_+^{-1})S^*T(b_-^{-1})f.
 \tag{13}
\]
Indeed the equation in (11) is equivalent to
\(ST(b_+)v=c^{-1}T(b_-^{-1})f\).
The range of \(S\) consists exactly of the sequences with zero
zeroth coordinate. The scalar \(c^{-1}\) is present in the
solution and cancels from the zero condition.
This proves every assertion, including the closed range.

The condition in (12) is a genuine nonzero bounded linear
functional of \(f\): \(T(b_-^{-1})\) is invertible.
Its vanishing is not implied by boundedness of the inverse of
the winding-zero factor \(T(A)\).

The reverse half-line has a different defect. Factor
\[
 B(z^{-1})=c\,b_+(z^{-1})\,z^{-1}b_-(z^{-1}).
 \tag{14}
\]
In this order the first factor is coanalytic and the last is
analytic. The corresponding Toeplitz factorization contains
\(S^*\), which is onto with a one-dimensional kernel.
Thus the reverse half-line is surjective with a one-dimensional
kernel. It requires a boundary choice for uniqueness rather than
the range condition (12).

More generally, after \(m>0\) net outward crossings of one
nonvanishing Laurent factor, the canonical middle term in
(9) is \(z^m\). The forward half-line has the \(m\) conditions
\[
                [T(b_-^{-1})f]_j=0,\qquad0\le j<m,
 \tag{15}
\]
and the reverse half-line has kernel dimension \(m\).
Multiplicity is included in this statement. No assertion of
only one condition survives further crossings without counting
them.

## 3. The full symbol retains a boundary defect

The product \(P=AB\) in (7) also has winding one. Factoring
its full polynomial directly as
\[
 P(z)=d\,p_-(z)\,z\,p_+(z),\qquad d\ne0,
 \tag{16}
\]
gives its own exact compatibility
\[
                    [T(p_-^{-1})f]_0=0.
 \tag{17}
\]
This is the range condition for the full shifted frozen model.
It is not automatically the same functional as (12).

In particular, the following finite boundary term cannot be
discarded. Write \(\Pi_+\) for projection from bilateral sequences
to indices \(n\ge0\), and \(\Pi_-=I-\Pi_+\). Laurent polynomials
act on the bilateral space by multiplication, equivalently
convolution. Then
\[
 \boxed{\quad
 T(P)=T(A)T(B)+K,\qquad
 K=\Pi_+A\Pi_-B\Pi_+ .
 \quad}
 \tag{18}
\]
In matrix form,
\[
 K_{n,k}=\sum_{\ell<0}A_{n-\ell}B_{\ell-k}.
 \tag{19}
\]
Because the actual bands are \([-6,5]\) and \([-5,6]\),
\[
                 K_{n,k}=0\quad\hbox{if }n>4\hbox{ or }k>4.
 \tag{20}
\]
Thus the defect is supported in the first five rows and columns
and has rank at most five. It is always nonzero. In fact the
only term in (19) at \(n=k=4\) has \(\ell=-1\), so
\[
 K_{4,4}=A_5B_{-5}
        =(w^3e^{5\lambda})(w^{-3}e^{-5\lambda})=1.
 \tag{20a}
\]
Here the extreme coefficients follow directly from the leading
and constant coefficients of \(\mathscr F_\pm\) in (1).

Since \(T(A)\) is invertible by its winding-zero factorization,
the equation \(T(P)v=f\) can equivalently be written as
\[
 T(B)v=T(A)^{-1}(f-Kv).
 \tag{21}
\]
Applying (12) now gives a condition containing the unknown
boundary vector \(Kv\). Replacing (21) by a condition on
\(T(A)^{-1}f\) alone would remove an actual boundary term.
The direct full factorization (16)--(17) avoids this replacement.

These statements are about fixed frozen scalar half-lines.
They do not identify a factorization of the finite grouped
operator \(\mathcal C_N\), prove an inverse after a symbol
crossing, or remove any of its eleven output modes.
The original full Hermite forcing identity belongs to
\(\mathcal C_N\), not separately to either principal factor.

## 4. Why even reflection does not remove the condition

Equation (4) shows that the factors exchange under simultaneous
angular and frequency reflection. A choice of the favorable
factor on positive frequencies must therefore be paired with
the opposite factor on negative frequencies to preserve the
original even space. The formulas above establish neither an
exact finite half-step operator with this property nor a
factorization of the original source on such an auxiliary space.

Even if such a factorization were obtained, the range and
boundary conditions would still have to be proved for its
actual right-hand side. A zero-free region for one principal
factor is not that compatibility statement. Nothing here
excludes a new parameter-dependent boundary construction or a
bilinear estimate retaining both factors.

## 5. The complete outgoing family spans its finite target

This separate statement uses the literal source, with no frozen
symbol approximation. Fix either parity and \(N\ge3\). Put
\[
 D=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M,\quad
 q=e^{i\pi/N},\quad r=q^{-2},\quad
 c_h=2\cos((2h+1)\pi/N),\quad s_h=2\sin(h\pi/N).
 \tag{22}
\]
Here \(\zeta\) is an independent formal spectral variable and
\(Z\) is the independent outgoing polynomial parameter.
The complete polynomials in the
[trailing determinant source](research_mixed_next_outgoing_trailing_determinants.md)
are
\[
 C_{b,N}(Z)=
 \sum_{k=0}^{D}
 \frac{r^{-bk}(r^{b+1};r)_k(rZ;r)_k}{(r;r)_k^2},
 \qquad M\le b\le D.
 \tag{23}
\]
Since \(r\) has exact order \(N\), every denominator in (23)
is nonzero for \(0\le k\le D\). If \(k>D-b\), its incoming
numerator contains \(1-r^N=0\). For \(0\le k\le D-b\),
all incoming exponents \(b+1,\ldots,b+k\) lie in
\(\{1,\ldots,D\}\), so those factors are nonzero.
The literal sum therefore stops exactly at
\(n_b=D-b\). Its terminal summand has leading coefficient
\[
 [Z^{n_b}]C_{b,N}(Z)
 =(-1)^{n_b}r^{-bn_b+n_b(n_b+1)/2}
       \frac{(r^{b+1};r)_{n_b}}{(r;r)_{n_b}^2}\ne0.
 \tag{24}
\]
Only that summand can contribute this degree. Empty products
at \(b=D\) give \(C_{D,N}=1\), so (24) includes the last row.

The original radical Newton quotients are
\[
 P_b^{\rm rad}(\zeta)
  =\prod_{h=M}^{b-1}\frac{c_h-\zeta}{s_{h+1}^2},
 \qquad \deg P_b^{\rm rad}=b-M.
 \tag{25}
\]
All denominators are nonzero: \(M+1\le h+1\le D\) for a
nonempty product. Their leading coefficients are
\[
 [\zeta^{b-M}]P_b^{\rm rad}
                  =(-1)^{b-M}\prod_{h=M}^{b-1}s_{h+1}^{-2}\ne0.
 \tag{26}
\]
The complete attached source, with its original signed row
phase, is exactly
\[
 F_N^+(\zeta,Z)=
       \sum_{b=M}^{D}(-q)^bC_{b,N}(Z)P_b^{\rm rad}(\zeta).
 \tag{27}
\]
This is the polynomial attached before the observation in the
[action-weighted Green theorem, Section 4](research_mixed_next_outgoing_action_weighted_green_ellipse.md).
Its degree in \(\zeta\) is exactly \(U\), since the last-row
coefficient is \((-q)^D\ne0\). The term with \(b=M\)
gives exact degree \(U\) in \(Z\). No large-level or saddle
approximation is used in (23)--(27).

**Finite span theorem.** For fixed \(N\), the polynomials
\[
              \{F_N^+(\,\cdot\,,Z):Z\in\mathbb C\}
 \tag{28}
\]
span all of \(\mathbb C[\zeta]_{\le U}\). The same is true
when \(Z\) is restricted to any nonempty open subset of
\(\mathbb C\).

To prove this, let \(\ell\) be a linear functional on the
target which vanishes on (28), or on such an open family.
Then the polynomial
\[
 \ell(F_N^+(\,\cdot\,,Z))
   =\sum_{b=M}^{D}(-q)^b\ell(P_b^{\rm rad})C_{b,N}(Z)
 \tag{29}
\]
vanishes identically. By (24), the polynomials \(C_{b,N}\)
have the distinct exact degrees \(U,U-1,\ldots,0\); hence
they form a basis of \(\mathbb C[Z]_{\le U}\).
All coefficients in (29) vanish. Equations (25)--(26)
show that the \(P_b^{\rm rad}\) form a basis of the target,
so \(\ell=0\). Finite-dimensional duality proves the claim.

More precisely, for any fixed proper linear subspace
\(V_N\subsetneq\mathbb C[\zeta]_{\le U}\), choose a nonzero
annihilator \(\ell\). Equation (29) is then a nonzero
polynomial of degree at most \(U\). Thus
\[
 \#\{Z\in\mathbb C:F_N^+(\,\cdot\,,Z)\in V_N\}\le U.
 \tag{30}
\]
The bound counts distinct values; it need not be sharp.
If \(\Pi\) is any fixed surjective linear map from this target
onto a finite-dimensional space \(E_N\), then
\(\operatorname{span}_Z\Pi F_N^+=E_N\). The same argument
gives (30) for membership in a fixed proper subspace of
\(E_N\). In particular this applies to a surjective fixed
cosine-degree compression.

This is not an assertion that a particular actual value \(Z_*\)
fails a compatibility, or that a signed pairing is nonzero.
It rules out only a parameter-independent proper range
containing the whole open complete outgoing family in its
specified finite target. It does not rule out a range depending
on \(Z\), a preimage with additional boundary data, or a
quantitative estimate which uses the two source phases together.
The cut-forcing and full Hermite identities remain those of the
adopted complete-source reduction; none is replaced by (12).

## Frozen source versions

- Degree-eleven factors, root counts and reciprocal conjugacy:
  b5793f83ec635753a592f6497787f7d11231f9fb15765c0ab6b718f6e4e1351d.
- Six endpoint roots and their strict ordering:
  aa0a17aec890cfe3951feaafd14a0c35b0d809a348181009e497cdc02dcdee90.
- Original zero-free finite inverse and Toeplitz convention:
  b499a21141be11650f30b94498626e01383c9493edd670e4ef38e5ec985e11d6.
- Complete source through the last physical row:
  8564c705a0c8cd96cb7211c10166a522dde511bda27a94ac18a7cdafccf0b47f.
- Exact complete attached Green polynomial and degree \(U\):
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.
