# A global analytic probe for every fixed signed odd inner crossing

Private exact-source theorem, 9 November 2026. The global analytic
probe extends to every fixed signed odd inner crossing \(n\) and
every fixed integer outer crossing \(p\). The proof supplies a
sufficient endpoint-zero polynomial of degree \(|n|\), establishes
ordinary divisibility from the original full jet maps, and proves
a nonzero principal multiplier on the entire real period.

The conclusion is an exact full-source identity with exponentially
small analytic residual. Its application retains the actual physical
norm of the inner source and its exact parity forcing. No geometric
packet, adequate action gap, or stability theorem for arbitrary
short fillings is inferred. No mathematical numerical evaluation
or frozen-source edit is used.

## 1. The full signed source and an ordinary realization

Fix
\[
n\in2\mathbb Z+1,\qquad p\in\mathbb Z,\qquad s=|n|\ge1.
\]
Both integers are fixed before the level tends to infinity.
Take \(N\) sufficiently large that
\[
m=\lfloor N/2\rfloor\ge s+1,\qquad N\ge6,
\]
and keep the original notation
\[
\begin{gathered}
D=N-1,\quad M=\lceil N/2\rceil,\quad U=m-1,\quad
\theta=\pi/N,\quad q=e^{i\theta},\quad \kappa=q^{D^2/2},\\
c_j=2\cos((2j+1)\theta),\quad
u_{j,N}=\pi-(2j+1)\theta,\quad z(u)=-2\cos u,\\
\mathcal A_N=\mathbb C[z]/(P_N),\quad P_N=2T_N(z/2)+2,\quad
\mathcal L=TZT,\quad\mathcal L_k=R^{-k}\mathcal LR^k .
\end{gathered}                                                     \tag{1}
\]
Here \(Z\) denotes spectral multiplication. All turns, crossings
and traces are the original full Hermite objects.

Set
\[
F_N^{\rm cap}=K_N^{\rm ord}(-2,\cdot),\qquad
Q_{n,N}=TR^nF_N^{\rm cap},\qquad
B_{j,N}=T\mathcal L_{-j}T,\qquad
\mathcal D_{n,N}=B_{n,N}+2I .
                                                                    \tag{2}
\]
The [signed odd-symbol source, equations (1)--(3)](research_odd_inner_crossings_positive_symbol.md)
proves the exact full-algebra equation
\[
\mathcal D_{n,N}Q_{n,N}=\mathfrak f_{n,N}1,\qquad
\mathfrak f_{n,N}=
\begin{cases}
4\kappa^n/N^2,&N\text{ even},\\
0,&N\text{ odd}.
\end{cases}
                                                                    \tag{3}
\]
This includes negative \(n\), without changing the complete-end
normalization.

For precision, choose ordinary realizations of \(B_{j,N}\) by
\[
\begin{gathered}
B_{0,N}=Z,\quad B_{1,N}=\mathcal L_1,\quad
B_{-1,N}=\mathcal L_{-1},\\
B_{j+1,N}+q^{-1}\mathcal L B_{j,N}
                  +q^{-2}B_{j-1,N}=8q^{-1}I.
\end{gathered}                                                     \tag{4}
\]
For positive indices solve forwards; for negative indices use
\(B_{j-1,N}=8qI-q\mathcal L B_{j,N}-q^2B_{j+1,N}\).
Every monomial in the resulting expression for \(B_{\pm s,N}\)
contains at most \(s\) factors of the form \(\mathcal L_k\).
Multiplications by \(Z\) do not count as shifts.

The transpose satisfies
\[
\mathcal D_{n,N}^{\rm t}=T\mathcal L_nT+2I
                       =\mathcal D_{-n,N}
\quad\hbox{in }\mathcal A_N .
                                                                    \tag{5}
\]
Define an ordinary polynomial operator \(\mathfrak B_{n,p,N}\)
by taking the chosen realization of \(B_{-n,N}+2I\) and making
the substitutions
\[
Z\longmapsto Z,\qquad \mathcal L_k\longmapsto\mathcal L_{p+k}.
\]
The original [crossing transport](research_current_free_aw_crossing_transport.md)
then gives
\[
\mathfrak B_{n,p,N}=R^{-p}\mathcal D_{n,N}^{\rm t}R^p
\quad\hbox{in the full algebra}.
                                                                    \tag{6}
\]
Each substituted \(\mathcal L_k\) is its original ordinary
polynomial realization. Thus \(\mathfrak B_{n,p,N}\) maps
ordinary polynomials to ordinary polynomials and has shift width
at most \(s\). Its ordered products are not replaced by commuting
symbols.

## 2. A sufficient endpoint polynomial from the full jet maps

The physical radical is \(e_M\mathcal A_N\): its elements vanish
at every distinct physical node, including the odd simple node.
For a radical element \(g\), denote its double-node angular
normals by
\[
p_j(g)=\left.\partial_u g(-2\cos u)\right|_{u=u_{j,N}}
                       =2\sin(u_{j,N})g'(c_j).
\]
For \(1\le r\le s\), say that \(g\) has an \(r\)-node zero collar if
\[
                       p_U(g)=\cdots=p_{U-r+1}(g)=0.
                                                                    \tag{7}
\]
The following is a sufficient propagation statement, not an
assertion that these are minimal endpoint conditions for every \(n\).

**Lemma 1.** For every integer \(k\), if \(g\) is radical and has
an \(r\)-node zero collar, then \(\mathcal L_kg\) is radical
and has an \((r-1)\)-node zero collar. When \(r=1\), only
radical membership is asserted. Spectral multiplication preserves
the radical and the same collar.

*Proof.* At a regular node, the original value of
\(\mathcal L_kg\) is a linear combination of the adjacent
values of \(g\), which are all zero. At the far node the
outward coefficient and its first derivative vanish, by the
original cubic zero. Thus no outside value or normal is introduced.

At the even coalescing node, the exact grouped formula from
[the endpoint source, equations (9),(15)](research_mixed_next_outer_adjoint_radical_endpoint_conditions.md)
gives, on a radical input,
\[
                    (\mathcal L_kg)(c_U)
                       =\frac8{\sin\theta}p_U(g).
\]
At the odd simple node its equations (12),(15) instead give
\[
(\mathcal L_kg)(-2)
 =-\frac{8q^k\cos^4(\theta/2)}{\sin\theta}p_U(g).
                                                                    \tag{8}
\]
These are zero under (7), at both parities; all other values
were already zero.

At a regular double node the output normal is a linear
combination of the input normals at that node and its two
neighbors, because every input value vanishes. Hence it is
zero on the last \(r-1\) nodes except possibly at a coalescing
position. The even grouped normal formula uses only \(p_U\)
and \(p_{U-1}\) when the input values vanish, and these are
both zero whenever the output collar includes \(U\).
At the last odd double node the same regular formula uses
the neighboring simple-node value and its identically zero
angular derivative; all other required normals again lie
in the input collar. This proves the normal assertion,
including \(r=2\).

Finally multiplication by \(z\) has normal
\(2\sin u_j\,g(c_j)+c_jp_j(g)\). It therefore preserves all
the stated zeros. Scalar multiplication does as well.
\(\square\)

Define the explicit ordinary polynomial
\[
\boxed{\qquad
Q_{s,N}^{\rm rev}(z)=\prod_{\nu=0}^{s-1}(z-c_{U-\nu}).
\qquad}                                                           \tag{9}
\]
If \(h=Q_{s,N}^{\rm rev}P\) is an ordinary polynomial, then
\(e_Mh\) is radical and its last \(s\) normals vanish.
Every monomial of \(\mathfrak B_{n,p,N}\) in (6) has at most
\(s\) shift factors. Applying Lemma 1 successively, while
retaining any intervening spectral multiplications, proves
that its output is radical. Hence
\(\mathfrak B_{n,p,N}(e_Mh)\) vanishes at every distinct
physical node. The ordinary polynomial \(e_M\) is a nonzero
multiple of the product of those distinct factors. Therefore
\[
\boxed{\quad
\frac{\mathfrak B_{n,p,N}(e_MQ_{s,N}^{\rm rev}P)}{e_M}
                           \in\mathbb C[z]
                  \qquad(P\in\mathbb C[z]).
\quad}                                                            \tag{10}
\]
This is ordinary divisibility without a degree restriction.
The odd simple value and all required coalescing first normals
were retained in its proof. There is no extra far-end condition,
and no vanishing of a derivative of \(P\) is required.

## 3. The regularized principal multiplier at both endpoints

Put \(E_N(u)=e_M(z(u))\). For even periodic functions define,
initially away from denominators,
\[
\mathcal C_{n,p,N}g
 =\frac{\mathfrak B_{n,p,N}
           (E_N Q_{s,N}^{\rm rev}(z(u))g(u))}{E_N}.
                                                                    \tag{11}
\]
The exact radical shift ratios remain
\[
\frac{E_N(u+2r\theta)}{E_N(u)}
=(-1)^r
\begin{cases}
1,&N\text{ even},\\
\sin((u+2r\theta)/2)/\sin(u/2),&N\text{ odd}.
\end{cases}
                                                                    \tag{12}
\]
The endpoint polynomial has the fixed-parity expression
\[
Q_{s,N}^{\rm rev}(z(u))
 =\prod_{\nu=1}^s2\{\cos(\lambda_{\nu,\mathrm{par}}\theta)-\cos u\},
\qquad
\lambda_{\nu,\mathrm{par}}=
\begin{cases}2\nu-1,&N\text{ even},\\2\nu,&N\text{ odd}.
\end{cases}
                                                                    \tag{13}
\]
Equations (4),(6),(12),(13) give an exact \(2s+1\)-shift
formula for (11), with real shifts of length at most
\(2\pi s/N\). Its raw poles are all real modulo \(2\pi\).
On compact nonreal horizontal strips the coefficients are
jointly analytic in \(u,N^{-1}\) after fixing parity.

The principal multiplier is
\[
\boxed{\qquad
m_{n,p}(u)=(2-2\cos u)^s d_n(u,-e^{ipu}),
\qquad}                                                           \tag{14}
\]
where \(d_n\) is the original symbol of the odd-inner source.
To check the character convention, its exact outer weights are
\[
\begin{split}
\mu_{j,N}^{(p)}
 &=(-1)^{U+(p+1)j}\kappa^p\omega_N(u_{j,N})q^{pj(j+1)},\\
\omega_N(u)&=
\begin{cases}
\sin u,&N\text{ even},\\
\sin u\sin(u/2)/\cos^2(\theta/2),&N\text{ odd},
\end{cases}\\
\frac{\mu_{i-r,N}^{(p)}}{\mu_{i,N}^{(p)}}
 &=(-1)^r e^{ipru_i+\pi ipr^2/N}
              \frac{\omega_N(u_i+2\pi r/N)}{\omega_N(u_i)} .
\end{split}                                                       \tag{15}
\]
Thus the principal constant-test weighted adjoint character is
\(-e^{ipu}\), precisely as in that source's equation (14).
In the regular interior the grouped full transpose in (11)
agrees with this weighted adjoint on physical values; the
factor (13) tends to \((2-2\cos u)^s\).
This proves (14) on the real open interval, and hence on its
regular analytic continuation. It also keeps the half-step
and the sign when \(p\) is even or negative.

Here is an explicit removal of the apparent singularity in (14).
Write \(t=u/2\), and define
\[
k=\cot t\cos(pt),\qquad h=-\sin(pt),\qquad
w_0=1,\quad w_1=k-h,\quad w_{j+1}=2kw_j+w_{j-1}
\quad(j\in\mathbb Z).
                                                                    \tag{16}
\]
The adopted exact square identity for signed odd \(n\) gives
\[
d_n(u,-e^{ipu})=4+4\cos^2t\,w_n^2 .
\]
Set \(W_{n,p}(u)=\sin^s t\,w_n\). For explicit denominator
control, define \(a_0=1,a_1=k,b_0=0,b_1=1\), and continue
both polynomial sequences by \(v_{j+1}=2kv_j+v_{j-1}\).
The same recurrence gives
\[
w_s=a_s(k)-h b_s(k),\qquad
w_{-s}=(-1)^s\{a_s(k)+h b_s(k)\},
\]
where \(\deg a_s=s\) and \(\deg b_s=s-1\).
Thus multiplication by \(\sin^s t\) cancels every possible
denominator, and \(W_{n,p}\) is an entire trigonometric polynomial.
The exact multiplier is
\[
\boxed{\quad
m_{n,p}(u)=4^{s+1}
 \left\{\sin^{2s}t+\cos^2t\,W_{n,p}(u)^2\right\}.
\quad}                                                            \tag{17}
\]
Its expression is even and \(2\pi\)-periodic. For example, under
\(u\mapsto-u\), both \(k,h\) change sign and \(w_n\) changes
by \((-1)^n=-1\), while \(\sin^s t\) also changes sign.
Under \(u\mapsto u+2\pi\), \(k,h\) both gain \((-1)^p\);
the square in (17) removes the resulting fixed sign.

As \(t\to0\), \(k=t^{-1}+O(t)\) and \(h=O(t)\).
Forward recurrence gives
\[
w_s=2^{s-1}t^{-s}+O(t^{-s+2}),
\]
and backward recurrence, starting at \(w_{-1}=-k-h\), gives
\[
w_{-s}=(-1)^s2^{s-1}t^{-s}+O(t^{-s+2}).
\]
Both statements include \(s=1\). Substituting in (17) proves
\[
\boxed{\qquad m_{n,p}(0)=16^s,\qquad
                    m_{n,p}(\pi)=4^{s+1}.\qquad}                  \tag{18}
\]
For real \(0<u<\pi\), the odd-symbol theorem gives \(d_n\ge4\).
Equations (14),(18), evenness and periodicity imply strict
positivity on the whole real circle. Consequently there are
fixed constants \(\mu_{n,p}>0\) and \(R_{n,p}>0\) such that
\[
|m_{n,p}(u)|\ge\mu_{n,p}
                  \qquad(|\Im u|\le R_{n,p}).
                                                                    \tag{19}
\]
These constants may depend on the fixed signed powers.
No estimate uniform in growing \(n,p\) is asserted.

## 4. The exact global analytic probe

Let \(\mathscr H_R^{\rm ev}\) be the bounded even
\(2\pi\)-periodic holomorphic functions on \(|\Im u|<R\),
with norm \(\|\cdot\|_R\).
The proof of the
[global three-source probe](research_mixed_next_outer_global_analytic_probe.md)
now applies with (10)--(19), as follows.

First, every such function is uniformly approximated on smaller
closed strips by finite cosine sums, which are ordinary
polynomials in \(z(u)\). Equation (10) makes each grouped
output an ordinary polynomial. On the two nonreal horizontal
boundary lines the finite shifts have no pole and stay on
those same lines. Passing to the limit and using the maximum
principle on the periodic annulus removes every grouped pole,
including the ones near both \(0\) and \(\pi\).
Thus \(\mathcal C_{n,p,N}\) maps even periodic analytic
functions to even periodic analytic functions on smaller strips.

Fix \(0<r<R<R_{n,p}\), with \(R-r<1\). The fixed-width
coefficient formula and its analytic dependence on \(N^{-1}\)
away from the real poles give, uniformly on both boundary lines,
\[
|a_{\nu,N}(u)|\le C,\qquad
|a_{\nu,N}(u)-a_{\nu,0}(u)|\le C/N,\qquad |\nu|\le s.
\]
Cauchy's derivative estimate on a strip enlarged by \(\delta\)
bounds the change of the input under each real shift by
\(4\pi s\|g\|_{t+\delta}/(N\delta)\).
Summing and using grouped removability proves
\[
\|(\mathcal C_{n,p,N}-m_{n,p})g\|_t
 \le\frac{C_{n,p,r,R}}{N\delta}\|g\|_{t+\delta},
\quad r\le t<t+\delta\le R,\quad0<\delta\le1.
                                                                    \tag{20}
\]
No central collar is removed in (20).

Choose a fixed
\[
A\ge\max\{1,C_{n,p,r,R}/\mu_{n,p}\},\quad
k_N=\left\lfloor\frac{(R-r)N}{4A}\right\rfloor,\quad
\mathcal T_N=(\mathcal C_{n,p,N}-m_{n,p})m_{n,p}^{-1}.
\]
The inverse multiplier is applied first. On nested strips with
successive loss \((R-r)/k_N\), each application has norm at
most \(1/4\). For \(F_N\in\mathscr H_R^{\rm ev}\), define
\[
g_N=m_{n,p}^{-1}\sum_{\ell=0}^{k_N-1}(-\mathcal T_N)^\ell F_N,
\qquad
\rho_N=(-\mathcal T_N)^{k_N}F_N,\qquad
h_N=Q_{s,N}^{\rm rev}(z(u))g_N .
                                                                    \tag{21}
\]
For all sufficiently large levels, these are defined on the
needed nested strips and satisfy
\[
\boxed{\quad
\mathcal C_{n,p,N}g_N=F_N-\rho_N,\qquad
\|g_N\|_r\le\frac4{3\mu_{n,p}}\|F_N\|_R,\qquad
\|\rho_N\|_r\le e^{-c_{n,p,r,R}N}\|F_N\|_R,
\quad}                                                            \tag{22}
\]
where one permissible fixed positive rate is
\[
c_{n,p,r,R}=\frac{(R-r)\log4}{8A}.
\]
These formulas are finite geometric identities, not an
assumed convergent infinite inverse. The test \(h_N\) has
all \(s\) zeros (9) exactly.

## 5. Full Hermite pairing and its actual source bound

Even periodic strip-holomorphic functions descend to
holomorphic spectral functions on an ellipse containing
\([-2,2]\). Interpret them in the full algebra by their
Hermite jets: values and first derivatives at double nodes,
and the value at the odd simple node.
Cosine-polynomial approximation on a larger strip passes
the original polynomial transpose to these analytic tests
at every fixed \(N\), including all endpoint jets.
There is no approximation cost or discarded boundary in
this exact limiting argument.

Define the original signed observation
\[
\mathcal O_{n,p,N}(F)
 =\phi_N[R^pe_MQ_{n,N}F],\qquad
\ell_{p,N}(h)=\phi_N[R^pe_Mh].
                                                                    \tag{23}
\]
Using (6),(11),(22) in the full transpose and then (3) gives
\[
\boxed{\qquad
\mathcal O_{n,p,N}(F_N)
 =\mathfrak f_{n,N}\ell_{p,N}(h_N)
                          +\mathcal O_{n,p,N}(\rho_N).
\qquad}                                                           \tag{24}
\]
The full source \(Q_{n,N}\), including its first normals,
is retained until the outer radical consumes them.
The odd simple-node implication is part of Lemma 1 and
the full Hermite limiting argument. Equation (24) has
no artificial interval or matching-boundary term.

Let \(q_{j,n,N}=Q_{n,N}(c_j)\), and keep the exact weights (15).
Then
\[
\ell_{p,N}(h_N)=\sum_{j=0}^U\mu_{j,N}^{(p)}h_N(u_{j,N}),
\qquad
\mathcal O_{n,p,N}(\rho_N)
 =\sum_{j=0}^U\mu_{j,N}^{(p)}q_{j,n,N}\rho_N(u_{j,N}).
                                                                    \tag{25}
\]
The crossing values have modulus one for all signed \(p\),
so \(|\mu_{j,N}^{(p)}|=\omega_N(u_{j,N})\le2\).
Also \(|Q_{s,N}^{\rm rev}(c_j)|\le4^s\).
Equations (3),(22),(25) give the complete quantitative
consequence
\[
\boxed{\quad
|\mathcal O_{n,p,N}(F_N)|
 \le C_{n,p,r,R}\|F_N\|_R
 \left\{N^{-1}
    +e^{-c_{n,p,r,R}N}
                 \sum_{j=0}^U|\mu_{j,N}^{(p)}q_{j,n,N}|\right\}.
\quad}                                                            \tag{26}
\]
At odd levels the \(N^{-1}\) forcing term is absent exactly.
No independent errors at the physical nodes were substituted
into the signed sum.

If a separate source theorem supplies
\(\max_j|q_{j,n,N}|\le C_\tau N^{A_\tau}e^{N(E_n+\tau)}\),
(26) gives a fixed positive gain relative to that ceiling
for polynomially bounded analytic inputs. It does not
supply such a sharp \(E_n\), a nonzero geometric coefficient,
or a comparison with the outer volume budget for a new \(n\).

For \(n=p=3\), (9),(14),(18) recover the adopted three-node
regularizer, the endpoint multiplier values \(4096,256\),
and the global probe. The extension above concerns every
fixed signed odd \(n\) and fixed signed or zero \(p\), with
constants permitted to depend on both. It does not extend
the positivity argument to even \(n\), and it makes no
claim that the sufficient endpoint polynomial is minimal
for every signed power.

This is one analytic ingredient for short-partial-filling
stability. The retained geometric source, its nonzero
coefficient, and sufficiently small competing contributions
remain separate requirements. Nothing here controls
unbounded tangle-template complexity or proves a
finite-exception statement.

## Source versions

- Signed odd-inner symbol and exact full forcing:
  7cb28ceade66edd8477715caec4a9204c2dcda0740e915fd6ccfcaeefa2c0eba.
- Original ordinary signed Askey--Wilson transports:
  f81b9fc3edc2504c5250ad283bf0ceff191a1fc3a310c00fdb57602362f0bf4a.
- Full arbitrary-power endpoint jet formulas used in Lemma 1:
  9cde443d65bfdc41104ffe9e78ce4e4540ec998b53681923f99fd42a5d436d71.
- Adopted whole-period analytic and Hermite approximation method:
  cb47c9d87949e276615443150b2da2260fec5bb09d3780039b90b322cd14eeb8.

