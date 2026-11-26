# An analytic small-meridian anchor for the original finite-color source

Private written proof, 18 November 2026.

The classical loop series in [C] is defined coefficient by coefficient.
This note proves directly that it is an asymptotic expansion of the
original finite-color polynomials on a small meridian domain. In
particular the leading reciprocal Alexander term is a locally uniform
limit of those polynomials, with their original cut and normalization.

The analytic Melvin--Morton--Rozansky theorem is established territory.
No novelty is claimed for that limit. The purpose is to obtain the
analytic starting estimate from the same literal source as our formal
and root-of-unity constructions. No external proof is used.

This is a neighborhood of meridian \(1\), not a continuation theorem to
an Alexander root or the complete root-of-unity point.

## 1. Statement and parameters

Fix the one-component \(b\)-strand braid of [C]. Its crossing count is
\(\ell\), its writhe is \(w\), and
\[
 m=b-1,\qquad c=b-1-w.
\]
For \(b=1\) the braid is empty and all assertions reduce to \(1=1\).
Assume \(b\ge2\), so \(m\ge1\).

Write \(h=\log Q\), with \(Q=q^2\). The natural meridian is
\[
 Y=e^u,\qquad x=\exp((u-h)/2).
\]
Let \(a_j(u)\) denote the coefficients of the canonical source of [C]
in this parameter:
\[
 \mathcal W_K(1-e^h,e^u)=\sum_{j\ge0}h^j a_j(u),
 \qquad a_0(u)=\Delta_K(e^u)^{-1}.                 \tag{1}
\]
In the argument of \(\mathcal W_K\), its first coordinate is
\(\delta=1-Q\). Thus (1) changes the quantum parameter explicitly.

**Theorem.** There is \(R>0\), depending only on the fixed braid,
such that
\[
 C_L(e^{u/(2L)})\longrightarrow\Delta_K(e^u)^{-1}
 \quad\text{uniformly for }|u|\le R
 \quad\text{as }L\longrightarrow\infty.           \tag{2}
\]
Here \(C_L\) is the original reduced, zero-framed color-\(L\)
polynomial. For each \(0<r<R\), constants \(K,A>0\) also satisfy
\[
 \left|C_L(e^{u/(2L)})
       -\sum_{j=0}^{J-1}(u/L)^j a_j(u)\right|
 \le K A^J J! |u/L|^J                           \tag{3}
\]
for every \(L\ge2\), \(J\ge1\), and \(r\le|u|\le R\).
All constants are independent of \(L,J,u\) in these ranges.

No value at \(u=2\pi i\) occurs in this theorem.

## 2. A transfer count forced by the one-component cut

Use the untruncated checked crossings of [C, (2)] and its ordinary
cut and pivot. In a fixed matrix path, denote the nonnegative transfer
at crossing \(d\) by \(n_d\). Follow the physical knot component from
the distinguished cut, whose index is zero.

At a positive crossing its two physical strands change indices by
\(-n_d\) and \(+n_d\); at a negative crossing the signs are reversed.
The swap in the checked matrix specifies which outgoing physical
strand to follow. Every crossing is encountered once on each strand
during the full traversal of the single closed component.

An intermediate index is therefore a partial signed sum of these
changes, starting at zero. It is at most the sum of all positive
changes, namely \(\sum_d n_d\). If
\[
 T=a_2+\cdots+a_b
\]
is the original external total index, this proves
\[
                         T\le m\sum_d n_d.       \tag{4}
\]
The argument applies to every untruncated closed path. It uses
one-component closure; it is not asserted for an arbitrary link cut.

## 3. A uniform bound on every finite total-index sector

For fixed \(T\), let
\[
 g_T(h,u)=x^c e^{-hT}
 \sum_{\substack{a_2+\cdots+a_b=T\\a_i\ge0}}
 \langle0,a_2,\ldots,a_b|B_\beta|
                  0,a_2,\ldots,a_b\rangle,
 \qquad x=e^{(u-h)/2}.                            \tag{5}
\]
It is an entire function of \(h,u\): each sector contains finitely
many Laurent-polynomial crossing entries.

Choose positive \(R,\rho\), put
\[
 s=e^{R+\rho}-1,\qquad
 a=s^{1/(2m)}(1+\sqrt s)^\ell
                  e^{\ell(R/2+\rho)},\qquad
 K_0=e^{|c|(R+\rho)/2+\rho}.                      \tag{6}
\]
We require \(s<1\), \(a<1\), and \(mR/\rho\le1/2\).
These choices exist: take \(\rho=4mR\) and then take \(R\)
sufficiently small. Shrink \(R\) further to avoid Alexander zeros
on \(|u|\le R\).

We claim that on the sector-dependent disk
\[
 |u|\le R,\qquad |h|\le\rho/(T+1)
\]
one has
\[
 |g_T(h,u)|\le
 K_0 {T+m-1\choose m-1}a^T.                     \tag{7}
\]

Every intermediate index is at most \(T\), by preservation of total
index. In a positive crossing, each color-product factor is
\[
 1-\exp(-u+h(a_{\rm in}-n+k+1)),\quad 0\le k<n.
\]
The integer multiplying \(h\) is between \(1\) and \(T\).
For a negative crossing the factors are
\[
 1-\exp(u+h(k-b_{\rm in})),\quad 0\le k<n,
\]
with that integer between \(-T\) and \(-1\).
Thus each factor has modulus at most \(s\).

The Gaussian polynomial has nonnegative integer coefficients, sum
\({a_{\rm in}\choose n}\) (or \({b_{\rm in}\choose n}\)), and degree
\(n(a_{\rm in}-n)\) (or \(n(b_{\rm in}-n)\)).
These statements follow by the finite \(Q\)-Pascal recurrence,
including the endpoint polynomials \(1\). Its modulus is consequently
at most its ordinary binomial coefficient times \(e^{\rho T/4}\).
The Cartan factor has modulus at most \(e^{\rho T/4}\), since both
relevant quadratic exponents are at most \(T^2/4\).
The remaining \(x\)-monomial contributes at most
\(e^{(R+\rho)T/2}\).

In the product over crossings retain the transfer factors \(s^{\sum n_d}\).
By (4),
\[
 s^{\sum n_d}
       \le s^{T/(2m)}(\sqrt s)^{\sum n_d}.         \tag{8}
\]
After this extraction, the column sum of the remaining binomial
transfer matrix is at most \((1+\sqrt s)^T\) at each crossing.
Its \(\ell\)-fold product has column norm at most
\((1+\sqrt s)^{\ell T}\). This bounds a sum over all matrix paths,
so in particular bounds the remaining closed paths.

The varying pivot \(e^{-hT}\) contributes at most \(e^\rho\).
The scalar \(x^c\) contributes at most \(e^{|c|(R+\rho)/2}\).
There are \({T+m-1\choose m-1}\) possible cut inputs.
Combining these estimates gives exactly (7).

## 4. The actual finite-color limit

Set \(h=u/L\). Then \(x=q^{L-1}\), so the finite-color restriction
proved in [C] applies before any specialization. Every surviving
intermediate index is less than \(L\), and therefore
\[
 C_L(e^{u/(2L)})
       =\sum_{T=0}^{m(L-1)}g_T(u/L,u).            \tag{9}
\]
For \(T\le m(L-1)\),
\[
 \frac{|u|}{L}\frac{T+1}{\rho}
          \le\frac{mR}{\rho}\le\frac12.
\]
Hence (7) bounds every term in (9), uniformly in \(L,u\).
The bound is summable over \(T\). For each fixed \(T\),
\(g_T(u/L,u)\) tends uniformly to \(g_T(0,u)\) on the closed
\(u\)-disk. Dominated convergence, first for a finite set of sectors
and then for their common tail, gives uniform convergence to
\(\sum_T g_T(0,u)\).

At \(h=0\) these are exactly the polynomial substitutions
\(\Gamma(L_\pm(e^{u/2}))\) of [C]. Their cut trace is
\[
 \sum_{T\ge0}g_T(0,u)\tau^T
       =\frac{e^{cu/2}}{D_\beta(e^{u/2},\tau)}.
\]
The absolute sector bound (7) permits evaluation at \(\tau=1\).
The original determinant identity
\(D_\beta(x,1)=x^c\Delta_K(x^2)\) proves (2).

## 5. Coefficients and the factorial remainder

Write \(g_{T,j}(u)=[h^j]g_T(h,u)\). Cauchy's estimate in (7) gives
\[
 |g_{T,j}(u)|\le
 K_0 {T+m-1\choose m-1}a^T
                         ((T+1)/\rho)^j.         \tag{10}
\]
For any \(\sigma>0\),
\((T+1)^j\le j!\sigma^{-j}e^{\sigma(T+1)}\).
Choose \(\sigma\) with \(ae^{2\sigma}<1\).
Equation (10) then proves absolute local uniform convergence of
the coefficient sum and bounds it by \(K_1 A_1^j j!\).
The rational trace identities of [C], followed by the explicit
change of quantum and meridian coordinates in (1), identify it:
\[
                         a_j(u)=\sum_{T\ge0}g_{T,j}(u).          \tag{11}
\]
One can first identify the two expressions for small \(\tau\);
the convergent coefficient sum and the rational function agree at
\(\tau=1\), since its determinant is nonzero here.

For \(T\le M_L:=m(L-1)\), Taylor's estimate on the same disk,
using the preceding radius ratio at most \(1/2\), gives
\[
 \left|g_T(u/L,u)
       -\sum_{j<J}(u/L)^j g_{T,j}(u)\right|
 \le 2K_0{T+m-1\choose m-1}a^T
                         ((T+1)|u/L|/\rho)^J .
\]
Summing this bound as above gives at most
\(K_2 A_2^J J!|u/L|^J\).

It remains to account for the coefficients in (11) with
\(T>M_L\), which do not appear in (9). Splitting \(a^T\) into
two equal powers and using (10) proves, for fixed positive
constants \(K_3,A_3,c_1\),
\[
 \sum_{T>M_L}|g_{T,j}(u)|
       \le K_3 A_3^j j! e^{-c_1 L},\qquad L\ge2.                \tag{12}
\]
For example \(c_1=-m\log(a)/4>0\) is valid, since
\(M_L\ge mL/2\). The remaining half of the geometric factor
absorbs the polynomial count and the factorial-moment bound.

If \(k=J-j\ge1\), the elementary exponential-series inequality gives
\[
 e^{-c_1L}\le\frac{k!}{(c_1L)^k}
       \le k!(c_1r)^{-k}|u/L|^k
       \quad\text{when }|u|\ge r.
\]
Apply this to each of the \(J\) terms \(j<J\) from (12), and use
\(j!(J-j)!\le J!\). Their sum is bounded by
\(K_4 A_4^J J!|u/L|^J\), enlarging \(A_4\) to absorb \(J\le2^J\).
Together with the low-sector remainder this proves (3).

## 6. What the anchor does and does not fix

The expansion is now tied to actual finite-color values on a small
complex meridian disk. The proof retains both crossing signs, the
one-component physical index path, the varying ordinary pivot,
the original cut, and zero framing.

The estimate (3) allows an exponentially small difference between
functions with the same formal expansion. It therefore does not
identify a particular Borel sum, select a nonabelian Stokes
coefficient, continue through an Alexander zero, or establish a
volume lower bound. In particular it cannot be evaluated at
\(u=2\pi i\) by substituting into a local asymptotic theorem.

The sole complete proof source is:

| Label | Complete source | SHA256 |
|---|---|---|
| C | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |

Its actual crossings, finite-color quotient, canonical coefficients,
and determinant normalization are used. The transfer inequality,
sector bounds, convergence, and remainder estimate are proved here.
Only written mathematics and source-text reads were used.
Frozen manuscripts and public documentation are unchanged.
