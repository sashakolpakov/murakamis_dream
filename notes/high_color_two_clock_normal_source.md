# Two actual clocks and the compact Frobenius source orbit

Research construction, 27 October 2026. The high integral color has
an exact whole source with a head clock and a Frobenius block clock.
The latter is invisible at the root but survives in its first quantum
normal. The divided-source orbit is the same twisted cotangent
surface as the compact coherent source, with its actual weight-N
prequantum clutch. These identities use original integral matrices,
not an abstract extra SL2 representation.

No identification of both internal geometric framing currents is
made. In particular, a Frobenius block index is not a crossing
transfer, and equality of low/high root periods does not equate their
whole quantum-normal lifts.

## 1. The canonical actual two-flag source retraction

Use [the high integral color](high_integral_color_frobenius_wall_source.md),
with dimension N(r+1), basis w_(k,s), 0<=k<=r, 0<=s<N,
q_N=exp(pi i/N), Q=q^2 and Z=Q^N. The actual whole divided matrices
give on each s-string

\[
 \Psi_s(q)=\exp(F^{(N)}(q))w_{0,s},\qquad
 \Lambda_s(q)=2^{-r}w_{0,s}^*\exp(\tau E^{(N)}(q)).
\]

Let Rw_(k,s)=k w_(k,s). Introduce independent source/dual coordinates
t,u and retain their normalization as an ACTUAL whole germ:

\[
 \begin{split}
 U_s(q;t,u)&=\Lambda_s(q)(tu)^R\Psi_s(q),\\
 I_{t,u}(q)e_s&=t^R\Psi_s(q),\\
 P_{t,u}(q)|_{s\text{-string}}
       &=U_s(q;t,u)^{-1}\Lambda_s(q)u^R.
 \end{split}                                                    \tag{1.1}
\]

Here P returns the scalar coefficient in the s-th head basis vector.
At the root

\[
 U_s(q_N;t,u)=2^{-r}(1+tu)^r.                         \tag{1.2}
\]

Thus on 1+tu!=0, these are regular whole source/co-source germs,
and P I=I_N exactly. All derivatives of U_s are retained. Their
normalized weights need not be binomial away from the root.

A chosen normalized head source and co-source may be attached to
this retraction. For example a head coherent parameter h gives
diagonal weights

\[
 H_s(h)={N-1\choose s}\frac{h^s}{(1+h)^{N-1}}.        \tag{1.3}
\]

This is an explicit ordinary polynomial coherent cut in the specified
head frame; transport the source and its dual together if a different
actual head basis is used. Their diagonal weights (1.3) are unchanged
by that diagonal frame transport. No claim that its ordinary SL2
action is the quantum braid action is required.

The resulting normalized functional on the actual high color is
\(\Phi_{h;t,u}(C)=\lambda_hP_{t,u}CI_{t,u}\psi_h\).
For the actual scalar high-color long-knot matrix it gives the SAME
whole ordinary color period C_(N(r+1))(Q), since lambda_h psi_h=1
and PI=I. At q_N this is K_N. The original external ADO modified
dimension line remains the one in the high-color source note.

## 2. The two-clock character is an exact whole rational expression

Let Jw_(k,s)=(kN+s)w_(k,s), and Sw_(k,s)=s w_(k,s). The fixed integer
floor is retained, and

\[
               J=S+NR,\qquad Q^J=Q^S Z^R.            \tag{2.1}
\]

Define A=Q^S and B=Z^R as actual diagonal operators. At the root
B=I, while A is the original nontrivial head clock. For all integer
a,b the source character is exactly

\[
 \Phi_{h;t,u}(A^aB^b)
   =\sum_{s=0}^{N-1}H_s(h)Q^{as}
                \frac{U_s(q;tZ^b,u)}{U_s(q;t,u)}.     \tag{2.2}
\]

Equation (2.2) is an identity of whole q-germs, including their
actual divided-factorial coefficients and normalization units.
It is not obtained by extending root binomial weights arbitrarily.

At q_N, (2.2) is independent of t,u and equals
\([(1+hQ_N^a)/(1+h)]^{N-1}\). Consequently a root observable depending
only on Q^J loses the independent Frobenius source coordinate.

## 3. Its first quantum normal recovers the block moment exactly

Write D_Q for Q partial_Q along the actual q-family, so D_Q is one
half of q partial_q. Put x=tu and

\[
                         \mu=r x/(1+x).
\]

For a diagonal insertion f(A,B) independent of q except through
these clocks, the exact first-normal identity is

\[
 \left.D_Q\Phi_{h;t,u}(f(A,B))\right|_{q_N}
   =\sum_sH_s(h)
       [sA\partial_A+N\mu B\partial_B]
                  f(A,B)|_{A=Q_N^s,B=1}.             \tag{3.1}
\]

Any explicit coefficient derivative of f must be added if present.
To prove (3.1), write the normalized s-string weights as w_(k,s)(q).
Their sum is exactly one, hence their derivatives sum to zero.
At the root f(A,1) is independent of k, so every derivative of the
WHOLE source/co-source weights cancels. The remaining clock derivative
is \(sA\partial_A+NkB\partial_B\). The root weights are
\({r\choose k}x^k/(1+x)^r\), whose mean is mu.
This cancellation does not set the individual source derivatives
to zero; many are nonzero in the exact audit.

In particular, for r>0,

\[
 \Phi(A)|_{q_N}=\left(\frac{1+hQ_N}{1+h}\right)^{N-1},
 \qquad
 \frac1{Nr}\left.D_Q\Phi(B)\right|_{q_N}
                                      =\frac{tu}{1+tu}.          \tag{3.2}
\]

The first depends nontrivially on h, and the second nontrivially on
x=tu. Their Jacobian in h,x is nonzero away from the explicit
denominators and the zero of 1+hQ_N. Thus root plus first-normal
data give TWO independent source coordinates, even though all
zeroth-order block-clock values are one. For the required r=N,
the normalization in the second expression is N^2 exactly.

The block number is intrinsic to the actual root divided action:
\(R=(r-[e_{\mathrm{cl}},f_{\mathrm{cl}}])/2\). Its clock satisfies
\(Bf_{\mathrm{cl}}B^{-1}=Zf_{\mathrm{cl}}\) and
\(Be_{\mathrm{cl}}B^{-1}=Z^{-1}e_{\mathrm{cl}}\).
These are literal finite matrix identities for the graded source,
not an assumed scalar holonomy character.

## 4. The actual divided-source orbit is the compact source surface

For r>=1, on the root multiplicity factor the source and dual are

\[
 \psi(t)=\sum_{k=0}^rt^kv_k,\qquad
 \lambda(t,u)(v_k)={r\choose k}\frac{u^k}{(1+tu)^r}.
\]

The actual divided generators in the high-color proof give exact
normalized moments

\[
 E=\lambda e_{\mathrm{cl}}\psi/r=\frac{t}{1+tu},\quad
 F=\lambda f_{\mathrm{cl}}\psi/r=\frac{u}{1+tu},\quad
 H=\lambda h_{\mathrm{cl}}\psi/r=\frac{1-tu}{1+tu}.          \tag{4.1}
\]

They satisfy H^2+4EF=1. These are single-insertion matrix moments,
not an assertion that products of expectations equal expectations
of products. The corresponding coadjoint projector convention is

\[
 \mathcal J(t,u)=
   2\frac{(1,t)^t(1,u)}{1+tu}-I
       =\begin{pmatrix}H&2F\\2E&-H\end{pmatrix},
 \qquad \mathcal J^2=I.                              \tag{4.2}
\]

Its marked eigenflags are (1,t) for +1 and (u,-1) for -1. For a
chosen meridian eigenvalue M the explicit matrix
\((M+M^{-1})I/2+(M-M^{-1})\mathcal J/2\) has determinant one,
trace M+M^(-1), and those marked eigenflags. This is a source moment
map to the meridian conjugacy class; it has not been identified
with the internal critical holonomy of the knot word.

Now set

\[
                   v=t,\qquad a=u/(1+tu),\qquad T=va. \tag{4.3}
\]

Then F=a, E=v(1-va), H=1-2va. The root source connection is obtained
directly by differentiating the actual source vector:

\[
        \lambda\,d\psi=\frac{r u\,dt}{1+tu}=r a\,dv,
                  d(\lambda d\psi)=-r\,dv\wedge da.   \tag{4.4}
\]

On the reciprocal chart t'=1/t,u'=1/u one has

\[
                   v'=1/v,\qquad a'=v-v^2a.           \tag{4.5}
\]

Thus the two source connection forms differ by r dlog v. The source
vectors themselves have clutch psi_n=v^r psi_s after basis reversal.
The coherent SOURCE VECTOR spans the tautological O(-r) line; its
dual co-source/polynomial line is O(r). The latter is the positive
prequantum line, with connection -lambda dpsi. Keeping both signs
explicit, this is the SAME affine cotangent torsor Conn(O(1)) as
the original compact source, with exact two-form dv wedge da and
its nontrivial affine clutch (4.5). For r=N the dual prequantum
weight is N, obtained from the actual divided source;
the original head half-form/degree-(N-1) line remains separate.

This goes beyond an abstract identification of two SL2 actions:
the variables, connection, clock generator T=R/r in its source
expectation, density chart, and transition are all explicit actual
matrix formulas. Its marked inverse/positive flags and dual/source
polarization have not been swapped silently.

### Actual divided commutators give exact compact-source currents

There is an exact current dictionary before any head partial trace.
Use the unnormalized dual row ell(u)_k=binom(r,k)u^k and put
sigma_r(C)=ell C psi/(1+tu)^r. Directly from the actual divided
matrix entries,

\[
 \begin{array}{lll}
 f_{\mathrm{cl}}\psi=\partial_t\psi,&
 e_{\mathrm{cl}}\psi=(rt-t^2\partial_t)\psi,&
 h_{\mathrm{cl}}\psi=(r-2t\partial_t)\psi,\\
 \ell e_{\mathrm{cl}}=\partial_u\ell,&
 \ell f_{\mathrm{cl}}=(ru-u^2\partial_u)\ell,&
 \ell h_{\mathrm{cl}}=(r-2u\partial_u)\ell.
 \end{array}                                                    \tag{4.6}
\]

The degree-r endpoints are exact: the top term is killed by
rt-t^2 partial_t, and the bottom by partial_t. Consequently

\[
 \begin{split}
 \sigma_r([e_{\mathrm{cl}},C])
       &=(\partial_u+t^2\partial_t)\sigma_r(C),\\
 \sigma_r([f_{\mathrm{cl}},C])
       &=-(\partial_t+u^2\partial_u)\sigma_r(C),\\
 \sigma_r([h_{\mathrm{cl}},C])
       &=2(t\partial_t-u\partial_u)\sigma_r(C).        \tag{4.7}
 \end{split}
\]

These vector fields preserve the exact compact two-form
dt wedge du/(1+tu)^2. The formulas extend entrywise when C has
actual head-matrix coefficients, so no scalar symbol or head
partial trace is assumed before deriving the currents.

One must retain the normalized source terms for one-sided actions.
For example

\[
 \begin{split}
 \sigma_r(e_{\mathrm{cl}}C)&=(\partial_u+rt/(1+tu))\sigma_r(C),\\
 \sigma_r(Ce_{\mathrm{cl}})&=(-t^2\partial_t+rt/(1+tu))\sigma_r(C),\\
 \sigma_r(f_{\mathrm{cl}}C)&=(-u^2\partial_u+ru/(1+tu))\sigma_r(C),\\
 \sigma_r(Cf_{\mathrm{cl}})&=(\partial_t+ru/(1+tu))\sigma_r(C).
 \end{split}                                                    \tag{4.8}
\]

Thus sigma is NOT being used as a multiplicative map to ordinary
functions. Its exact left/right differential actions or corresponding
star product transport matrix products. An actual Frobenius
enveloping-degree-d operator has by (4.6)--(4.8) a differential
realization of order at most d, with polynomial r-degree at most d.
This is the explicit source adapter available for a bounded-degree
normal crossing/current calculation. A proof that the actual mixed
normal crossing operators produce the TWO required geometric
framing currents is still needed.

Whole block clocks also have an exact source action. For
B_xi=xi^R and a matrix C independent of t,u,

\[
 \begin{split}
 \sigma_r(CB_\xi)(t,u)
    &=\left(\frac{1+\xi tu}{1+tu}\right)^r
                               \sigma_r(C)(\xi t,u),\\
 \sigma_r(B_\xi C)(t,u)
    &=\left(\frac{1+\xi tu}{1+tu}\right)^r
                               \sigma_r(C)(t,\xi u),\\
 \sigma_r(B_\xi C B_\xi^{-1})(t,u)
    &=\sigma_r(C)(\xi^{-1}t,\xi u).                   \tag{4.9}
 \end{split}
\]

Thus a head/block clock gauge can be transported as exact finite
dilations, retaining its source character, rather than expanded as
a polynomial Fr operator of falsely bounded degree. Its first
normal generator is the Cartan moment already proved in (3.1).

## 5. The remaining source and holonomy comparisons

The off-root color still follows
M_high=-q^(N(r+1)), Y_high=Z^(r+1), whereas the original N-color
path follows Y_low=Z. All powers q^N and M^N, including the
high-color lift sign, remain in the original whole source and
external peripheral line. Formula (3.1) does not equate these paths.

Nor is R a literal crossing transfer. A total position is s+Nk;
a crossing transfer is a difference of such total positions.
The transparent root multiplicity braid merely permutes its block
labels, so its block-transfer difference is zero at zeroth order.
The mixed normal crossing/coproduct and the two-current coupling
are needed to relate the new source variables to the TWO internal
geometric framing flows. The explicit first-normal block arrows
in the high-color proof are part of that map, not its conclusion.

At 1+tu=0, the coherent normalization vanishes. The actual units
U_s in (1.1) must be retained before taking any simultaneous normal
or meridian limit. The compact source identification above does
not permit evaluating a separately canceled root expression at
that source wall or infer a regular geometric period there.

[Exact two-clock/source audit](../experiments/audit_high_color_two_clock_source.py).
[Results](../experiments/high_color_two_clock_source_results.json).
