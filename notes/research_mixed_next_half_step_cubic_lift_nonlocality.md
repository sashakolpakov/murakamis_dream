# A locality obstruction for the exact cubic half-step lift

Private exact-source deduction, 9 November 2026. The regular doubled-grid
factor has an exact full-Frobenius source lift. Its cubic off-diagonal
map nevertheless cannot be a uniformly finite-stencil operator on the
original physical jets: every nonzero ordinary output row requires
linearly many original nodes. This identifies a limitation of that
specific turn-conjugated factor, without ruling out a different doubled
factorization or a source-specific cancellation argument.

No mathematical numerical evaluation or frozen-source change is used.

## 1. The exact map and its range

Use \(N\ge3\), \(D=N-1\), \(m=\lfloor N/2\rfloor\),
\(M=\lceil N/2\rceil\), \(U=m-1\), and
\(\theta=\pi/N\). The original and opposite spectral algebras are
\[
 \mathcal A_0=\mathbb C[X]/(P_N),\qquad
 \mathcal A_4=\mathbb C[X]/(P_N-4),\qquad
 P_N=2T_N(X/2)+2.
\tag{1}
\]
Their canonical representatives have degree less than \(N\).
Retain the original Newton basis
\[
 e_j(X)=S_j^{-2}\prod_{a<j}(c_a-X),\qquad
 S_j=\prod_{a=1}^j2\sin(a\theta),\quad S_0=1,\qquad
 c_a=2\cos((2a+1)\theta),\qquad Te_j=e_{D-j},
\tag{2}
\]
and the original invertible crossing \(R\), with all its first
normals. From the [regular half-step calculus](research_mixed_next_outer_regular_half_step_calculus.md)
and [full-Frobenius source lift](research_mixed_next_half_step_frobenius_source_lift.md),
put
\[
 S=4\sin\theta\,(1-X/2)\mathsf D,
 \qquad
 \mathcal K=S R^{-3}T:\mathcal A_0\longrightarrow\mathcal A_4.
\tag{3}
\]
This is exactly the lower off-diagonal map in the cubic doubled-source
lift. Its full-domain meaning is already fixed by the cited polynomial
and quotient identities.

The ordinary divided difference has degree multipliers
\(\sin(j\theta)/\sin\theta\) at degrees \(1\le j<N\), all
nonzero. It is therefore a surjection from degree-\(<N\)
polynomials onto degree-\(<N-1\) polynomials, with kernel the
constants. Multiplication by \(1-X/2\) then gives exactly the
degree-\(<N\) polynomials vanishing at \(X=2\). Since this
is a simple node of the opposite grid at both parities,
\[
 \operatorname{ran}S=\operatorname{ran}\mathcal K
        =\{h\in\mathcal A_4:h(2)=0\},
 \qquad \operatorname{rank}\mathcal K=N-1.
\tag{4}
\]
The equality of ranges uses invertibility of \(R^{-3}T\).
For every opposite spectral node \(d\ne2\), the functional
\(f\mapsto(\mathcal Kf)(d)\) is nonzero: its range contains
the polynomial \(X-2\).

## 2. Exact annihilation of all low-degree input values

**Lemma 1.** If the canonical polynomial \(f\) has degree at
most \(M-2\), then
\[
                 (\mathcal Kf)(d)=0
       \quad\text{at every distinct opposite spectral node }d.
\tag{5}
\]
This asserts only ordinary output values, not their first normals.

*Proof.* Triangularity of the original Newton basis gives
\[
 Tf\in\operatorname{span}\{e_j:j\ge D-(M-2)\}.
\tag{6}
\]
At \(N=2m\), the lower index in (6) is \(m+1\).
Every such \(e_j\) vanishes at all original physical nodes and
has zero first normal at the central double node
\(c_{m-1}=c_m=-2\cos\theta\): both copies of that root occur
among its factors. At \(N=2m+1\), the lower index is also
\(m+1=M\). Every such \(e_j\) lies in the full radical:
it vanishes at every original double node and at the original
simple node \(-2\).

Multiplication by \(R^{-3}\) preserves all these vanishing
conditions. In particular, a zero value and first normal remain
zero under multiplication, and a simple zero value remains zero.
Let \(h=R^{-3}Tf\) be its full canonical class.

An opposite interior node has the form
\(d_r=2\cos(2r\theta)=-2\cos u_r\), with
\(u_r=\pi-2r\theta\in(0,\pi)\). Its two half-shifts
\(u_r\pm\theta\) are original physical angles, including the
original simple endpoint if one of them is zero. The regular formula
\[
 \mathsf D h(-2\cos u_r)
    =\frac{h(-2\cos(u_r+\theta))
                -h(-2\cos(u_r-\theta))}
                  {4\sin\theta\sin u_r}
\tag{7}
\]
therefore vanishes, since both numerator values vanish.

At the opposite simple endpoint \(+2\), the factor \(1-X/2\)
in (3) kills the value. The only other possible opposite endpoint
is \(-2\), occurring when \(N\) is even. Its regular divided
difference is
\[
      \mathsf D h(-2)=h'(-2\cos\theta)=0
\tag{8}
\]
by the even first-normal condition just proved. These cases exhaust
both opposite grids, proving (5). \(\square\)

The even first normal in (8) is necessary for this proof. Distinct
node values alone would not establish the endpoint statement.

## 3. The required number of original jet locations

Fix any opposite spectral node \(d\ne2\). Consider a representation
of its output functional using only a set \(J\) of original physical
nodes and their full available jets:
\[
 (\mathcal Kf)(d)
    =\sum_{j\in J_{\rm dbl}}
          \{a_jf(c_j)+b_jf'(c_j)\}
       +\mathbf 1_{\{-2\in J_{\rm simp}\}}\,a_* f(-2).
\tag{9}
\]
The final term is available only at odd levels. The coefficients may
depend arbitrarily on \(N\) and \(d\). Whenever a first normal is
allowed at a double node, count its value as part of the same local
Hermite data, even if its coefficient in (9) is zero. Thus the number
of local jet slots is
\[
                   n_J=2|J_{\rm dbl}|+|J_{\rm simp}|.
\tag{10}
\]

**Theorem 2.** Every representation (9) of this nonzero functional
must satisfy
\[
                  n_J\ge M,
       \qquad |J|\ge\lceil M/2\rceil.
\tag{11}
\]

*Proof.* If \(n_J\le M-1\), ordinary Hermite interpolation on
these distinct physical nodes realizes arbitrary data in (10) by
a polynomial of degree at most \(n_J-1\le M-2\). Lemma 1
says the left side of (9) vanishes on every one of those polynomials.
Therefore every coefficient in (9) is zero. This contradicts the
nonzero functional established in (4). The first assertion follows;
each original node contributes at most two slots, giving the second.
\(\square\)

In particular no number of original jet locations independent of
\(N\) can realize the ordinary output rows of this exact cubic
off-diagonal map. This includes finite-stencil angular formulas with
all coalescing first normals correctly grouped. A formula using
off-grid samples or nonlocal canonical interpolation is not such a
finite-stencil representation and is not ruled out by (11).

The obstruction concerns the specific lift (3). It does not exclude a
different matrix factorization, a different auxiliary module, or an
additional identity satisfied only by the actual test or source. The
full-Frobenius observation identity remains exact. What (11) prevents
is treating its turn-conjugated factor as an already local realization
of one favorable oriented principal factor.
