# Polynomial level dependence of the original Verma Gevrey type

Private written proof, 17 November 2026. The actual all-root source
of [G] has a Gevrey-1 type bounded by C N log(eN), rather than an
exponential in N, when the classical meridian x0^N stays in a
fixed compact set away from Alexander poles. The prefactor is
a fixed power of N times exp(CN). The constants below are explicit.

The proof estimates the genuine signed crossings on finite
total-index sectors. It keeps their head residues, factorial
zeros, carries, ordinary pivot and prescribed cut. A full color
cycle is estimated through its nearest root factor; it is not
replaced by independent absolute bounds on its N factors.
The moving grading circle then approaches grading one at rate
1/N. No analytic summation or nonzero closed-period conclusion
is asserted.

## 1. Source and uniform statement

Retain the source of [G]. A fixed braid beta has b>=2 strands,
one-cycle permutation, ell signed crossings and writhe w.
Put m=b-1 and c=b-1-w; c is even. For every N>=2,
\[
 q_0=e^{\pi i/N},\quad \zeta=q_0^2,\quad
 \delta=1-Q^N,\quad q=q_0(1-\delta)^{1/(2N)},\quad Q=q^2.
                                                               \tag{1}
\]
The logarithm at delta=0 is fixed. The literal entries are
\[
\begin{split}
 R^+_{v+n,u-n;\,u,v}
 &=x^{-u-v+n}Q^{(u-n)v}{u\brack n}_Q
                 (x^{-2}Q^{u-n};Q)_n,\quad 0\le n\le u,\\
 R^-_{v-n,u+n;\,u,v}
 &=x^{u+v-n}Q^{-uv}{v\brack n}_Q
                 (x^2Q^{1-v};Q)_n,\quad 0\le n\le v.
\end{split}                                                    \tag{2}
\]
Their word product is B_beta. With the original cut index zero,
\[
 V_\beta(q,x;\tau)=x^c\sum_{a_2,\ldots,a_b\ge0}
 \tau^TQ^{-T}
 \langle0,a_2,\ldots,a_b|B_\beta|0,a_2,\ldots,a_b\rangle,
 \qquad T=\sum_{i=2}^b a_i.                                    \tag{3}
\]
Each grading coefficient is a finite sum.

Let K be a nonempty compact subset of C* such that
Delta_Knot(k^2) is nonzero on K. The notation Delta below means
this normalized Alexander polynomial, not the compact set.
Define
\[
 U=\sup_{k\in K}|\log|k||,\qquad
 d=\inf_{k\in K}|k^c\Delta(k^2)|>0.                             \tag{4}
\]
For every N allow ALL x0 with x0^N in K; in particular no
restriction on the phase of x0 is imposed. Consider separately
the two source paths
\[
\begin{split}
 V^{\mathrm x}(\delta,x_0;\tau)&=V_\beta(q(\delta),x_0;\tau),\\
 V^{\mathrm M}(\delta,x_0;\tau)&=
 V_\beta(q(\delta),x_0(1-\delta)^{-1/(2N)};\tau).
\end{split}                                                    \tag{5}
\]
The second holds the original meridian M=-q0 x0 fixed.
Write V_j^x and V_j^M for their delta coefficients, rationally
continued in tau as in [G]. Their values at tau=1 are the same
canonical normal completions specified there, on the respective
normal paths.

Here are constants used in the theorem. They are independent
of N and j:
\[
\begin{gathered}
 \rho=1/32,\quad W=U+1,\quad p=\ell+m-1,\qquad
 P=1+e^{W+2\rho},\quad J=e^W(2W+\pi),\\
 K_{\mathrm{cyc}}=
 e^{2W}(J+4e^W\rho)\exp(4\rho e^{3W/2}),\\
 a=2+\log P,\qquad b_0=3+W+\log K_{\mathrm{cyc}},\qquad
 s=\ell b_0+1,\\
 H=(1+3^\ell e^{2W\ell})^m,\qquad
 K_{\mathrm{src}}=\exp(W|c|/2+2\rho),\\
 A_0=3e^{1/2}4^p p!\,K_{\mathrm{src}}e^{\ell b_0},\\
 C_0=A_0(m+1)H d^{-1}e^{ms},\qquad
 C_1=12\rho^{-1}H^2d^{-2}e^{2ms}.
\end{gathered}                                                    \tag{6}
\]

**Theorem.** For either normal path in (5), every N>=2,
every x0^N in K and every j>=0,
\[
 |V_j^{\mathrm x}(x_0,1)|,\ |V_j^{\mathrm M}(x_0,1)|
 \ \le\
 C_0N^{p+2}e^{\ell aN}
           \bigl(C_1N\log(eN)\bigr)^j j!.                       \tag{7}
\]
For the complete original meridian M=1, x0=-q0^(-1) has
x0^N in {1,-1}. Take K={1,-1}, so U=0 and d=1.
Thus (7) applies with constants depending only on the word.
It also applies to fixed x at that root point, but those
normal coefficients are not identified with fixed-M normals.

The b=1 word is empty and (3) is 1, so its conclusion is immediate.
The subsequent proof assumes b>=2.

## 2. Root heads and the factorial units

Write L_N=log(eN). Two elementary root estimates will be used:
\[
 \sum_{r=1}^{N-1}|1-\zeta^r|^{-1}\le \tfrac12 NL_N,\qquad
 e^{-N/2}\le |p_h|\le2^N,\quad
 p_h=\prod_{r=1}^h(1-\zeta^r),\quad 0\le h<N.                   \tag{8}
\]
For the first, pair r with N-r and use
|1-zeta^r|>=4 min(r,N-r)/N and the harmonic-sum bound
sum_{r<=n}1/r<=1+log n. For the second, the upper bound is
immediate. Every partial product is at least the product of
min(1,|1-zeta^r|) over all residues. The increasing function
f(t)=log min(1,4t/N) has integral -N/4 on [0,N/2].
Its right-endpoint sum is at least that integral. Pairing the
two halves therefore bounds the logarithm of this latter
product below by -N/2. This includes N=2 and proves (8)
without an asymptotic factorial formula.

Fix a total index T and put S=T/N, retaining zeta from (1).
All intermediate indices in (2) are at most T. Work on
\[
 |\delta|\le R_T=\frac{\rho}{NL_N(S+1)},\qquad
 \eta=\log(1-\delta),\qquad |\eta|\le2|\delta|.                  \tag{9}
\]
For every integer 0<=h<=T, factor its full root zeros:
\[
 (Q;Q)_h
  =\delta^A A!N^A p_r\,U_h(\delta),\qquad
  h=NA+r,\quad 0\le r<N,\quad U_h(0)=1.
                                                               \tag{10}
\]
The unit and its inverse satisfy
\[
                  |U_h|,\ |U_h|^{-1}
                         \le\exp(8\rho(S+1)).                  \tag{11}
\]
Here is a direct proof retaining all endpoints.

For a nonzero residue, the absolute difference of its ratio
to the root factor from 1 is at most
\[
              \frac{4|\delta|(S+1)}{|1-\zeta^r|}.
\]
Indeed Q^h=zeta^h exp(eta h/N), and |eta h/N|<=2|delta|S.
The displayed relative error is at most rho/L_N by (8), hence
less than 1/2. Its logarithmic modulus in either direction is
bounded by twice that error. Each residue occurs at most S+1
times, so (8) bounds their total contribution by 4rho(S+1).

At a root-zero factor h=Nl, its quotient by l delta is
\[
 \frac{1-(1-\delta)^l}{l\delta}
                 =\frac1l\sum_{v=0}^{l-1}(1-\delta)^v.
\]
Its difference from 1 is at most 2l|delta|, and its logarithmic
modulus in either direction at most 4l|delta|. Summing l<=A
costs at most 2|delta|A(A+1), which is at most
2rho(S+1). Thus (11) is a conservative common bound.
The nonzero factors in one complete root cycle have product N,
so this proves both (10) and (11) on the whole disk.

For an actual Gaussian in (2), write its top index u=NA+r
and transfer n=NC+t. Set e=1 if t>r, and e=0 otherwise.
Then u-n=N(A-C-e)+r-t+Ne. Formula (10) gives exactly
\[
 {u\brack n}_Q
 =\delta^eN^e{A\choose C}(A-C)^e
   \frac{p_r}{p_t p_{r-t+Ne}}\,
   \frac{U_u}{U_nU_{u-n}}.                                    \tag{12}
\]
When e=1 the actual range has C<=A-1. Thus the endpoint
factor A-C and its root-zero valuation have not been dropped.
By (8)--(11),
\[
                         \left|{u\brack n}_Q\right|
                             \le e^{2N+2(S+1)}.                \tag{13}
\]
To see the constants explicitly, the head ratio is at most
exp((1+log2)N), the binomial is at most 2^A, the unit quotient
costs exp(24rho(S+1)), and
N|delta|(A-C)<=rho/L_N<=1. These are bounded by (13).
The same proof applies to the Gaussian with top index v in
the negative crossing.

## 3. One complete color cycle

We prove a bound uniform over all phases, including a root
zero. Let alpha=x0^(2) or x0^(-2). Then
\[
                    e^{-2W/N}\le|\alpha|\le e^{2W/N}.
\]
Choose a residue r0 for which the phase of alpha zeta^r0 is
closest to 1, so its principal argument lies in [-pi/N,pi/N].
With J as in (6),
\[
                         |1-\alpha\zeta^{r_0}|\le J/N.
                                                               \tag{14}
\]
This follows from
||alpha|-1|<=2W e^W/N and the chord bound for that argument.

For every other residue whose cyclic distance from r0 is k,
1<=k<=floor(N/2), its angular distance from 1 is at least
pi(2k-1)/N. The identity
\[
 |1-re^{i\theta}|^2=(1-r)^2+4r\sin^2(\theta/2)
\]
and the chord bound give
\[
 |1-\alpha\zeta^r|\ge
           2e^{-W/2}(2k-1)/N.
\]
Each k occurs at most twice. Consequently, including N=2,
\[
             \sum_{r\ne r_0}|1-\alpha\zeta^r|^{-1}
                       \le e^{W/2}NL_N.                       \tag{15}
\]
The product of these OTHER factors is the exact polynomial
\[
 \prod_{r\ne r_0}(1-\alpha\zeta^r)
       =\sum_{h=0}^{N-1}(\alpha\zeta^{r_0})^h,
 \qquad
 \left|\prod_{r\ne r_0}(1-\alpha\zeta^r)\right|
                              \le N e^{2W}.                    \tag{16}
\]
The removable case alpha zeta^r0=1 is included; no division
by its zero factor is made.

In either color product in (2), the root labels form a
consecutive integer interval. On the fixed-x path a factor is
1-alpha zeta^v exp(eta v/N), with |v|<=T. On the fixed-M path
its varying exponent is (v+1)/N or (v-1)/N instead. Thus in
both cases its difference from its root value is at most
\[
                           \epsilon=4e^W|\delta|(S+1).
\]
For a full consecutive N-cycle use (14) on the chosen factor,
and apply 1+t<=exp(t) with (15) to the other factors. Equations
(9), (14)--(16) give
\[
\begin{split}
 \left|\prod_{\text{one full cycle}}
                     (1-\text{actual color factor})\right|
 &\le (J/N+\epsilon)\,N e^{2W}
           \exp(\epsilon e^{W/2}NL_N)\\
 &\le e^{2W}(J+4e^W\rho)\exp(4\rho e^{3W/2})
   =K_{\mathrm{cyc}}.                                        \tag{17}
\end{split}
\]
In the first line, “actual color factor” means the alpha-times-
root-times-exponential inside the corresponding factor of (2).
The estimate includes any block start; its exponent bound uses
the original total T.

A remaining interval of fewer than N factors has modulus at
most P^N, because each factor has modulus at most
P=1+exp(W+2rho). Splitting either actual length-n color product
into floor(n/N) full cycles and a final partial interval yields
\[
 |\text{color product}|
                    \le P^N K_{\mathrm{cyc}}^{\,S}.             \tag{18}
\]
Since K_cyc>1 and n<=T, this is valid without rounding losses.
This is the cancellation of N-factor growth used in the proof.
It is a bound on the full product with its nearest factor
retained, not a claim that the factors are positive.

## 4. Finite-sector source bound and moving grading circle

For either path in (5), the x monomial in a crossing has
modulus at most exp(WS). For the second path this uses
x=x0 exp(-eta/(2N)) and |eta|<=2rho. Each Cartan factor has
modulus at most exp(rho(S+1)), since its exponent has absolute
value at most T^2/4 and
\[
 |\log|Q||\le 2|\delta|/N.
\]
There are at most T+1 possible transfers in an input column.
Combining (13), (18) and these estimates proves, on (9),
\[
 \|R^\pm\|_{1,T}
           \le (T+1)\exp\{aN+b_0(S+1)\}.                       \tag{19}
\]
This is the actual finite-sector column-sum norm. Both signs
are estimated by their literal entries, not by a norm bound
for an inverse. All factorial and color endpoints were retained.

After ell crossings, multiply these bounds. There are at most
(T+1)^(m-1) closed input tuples, since their first m-1 indices
determine the last. The pivot Q^(-T) has modulus at most
exp(2rho); the source factor x^c at most exp(W|c|/2).
Writing v_T for the coefficient of tau^T on either path gives
\[
 |v_T(\delta,x_0)|\le
 K_{\mathrm{src}}e^{\ell aN}(T+1)^p
                       e^{\ell b_0(S+1)}.                     \tag{20}
\]
In particular this estimates the original closing itself,
rather than a modified finite state.

Cauchy's estimate on (9) multiplies (20) by
\[
                        \bigl(NL_N(S+1)/\rho\bigr)^j.
\]
Now choose the grading circle
\[
                           t_N=e^{-s/N},\qquad s=\ell b_0+1.
                                                               \tag{21}
\]
For |tau|<=t_N the remaining exponential in S is exp(-S),
apart from the constant exp(ell b0). Also T+1<=N(S+1).
The elementary estimates
\[
\begin{split}
 (S+1)^{j+p}&\le (j+p)!2^{j+p}e^{(S+1)/2},\\
 (j+p)!&\le2^{j+p}j!p!,\\
 \sum_{T\ge0}e^{-T/(2N)}&\le3N
\end{split}
\]
therefore give the absolutely convergent coefficient bound
\[
 |V_j^{\mathrm x}(x_0,\tau)|,\ |V_j^{\mathrm M}(x_0,\tau)|
 \le
 A_0N^{p+1}e^{\ell aN}
              \bigl(4NL_N/\rho\bigr)^j j!,
 \qquad |\tau|\le t_N.                                      \tag{22}
\]
No analytic delta germ is claimed on a common disk for the
untruncated sum. Cauchy was applied to each finite coefficient
on its own disk (9), then its order-j bounds were summed.

## 5. Rational propagation to grading one

For either normal path, [G] gives the exact rational form
\[
 V_j(x_0,\tau)=
 \frac{P_j(x_0,\tau)}{D_N(x_0,\tau)^{2j+1}},\qquad
 \deg_\tau P_j\le d_j=m(N-1)+2jNm,                             \tag{23}
\]
where
\[
 D_N(x_0,\tau)=
       \det(I-\tau^N A_\beta(x_0^N)).
\]
Here A_beta is the deleted classical matrix of the original
word. The fixed-M degree bound already includes the Euler-x
chain rule; the two paths need not have the same numerator.
The head-grading term m(N-1), all closed carries, and the
ordinary pivot are included in (23).

On the scaled annulus the elementary row-sum norm satisfies
||A_beta||_infty<=3^ell exp(2W ell). Thus on |tau|=t_N,
\[
                              |D_N|\le H.                     \tag{24}
\]
The small-circle coefficient series in (22) and the rational
identity imply the corresponding polynomial numerator bound,
even if a determinant zero there is removable.

For a polynomial p0 of degree at most d_j, Cauchy's coefficient
formula, with t_N<1, gives
\[
 |p_0(1)|\le(d_j+1)t_N^{-d_j}
                          \sup_{|\tau|=t_N}|p_0(\tau)|.
                                                               \tag{25}
\]
This retains the moving radius. Replacing 1/t_N by a fixed
number greater than 1 would lose the claimed level dependence.
Since
\[
 d_j+1\le(m+1)N(2j+1)\le(m+1)N3^j,\qquad
 t_N^{-d_j}\le e^{ms(2j+1)},
\]
the cost of (25) is a fixed power of N times a constant to
the j-th power.

Finally the exact source normalization is
\[
             D_N(x_0,1)=(x_0^N)^c\Delta((x_0^N)^2),
\]
whose modulus is at least d in (4). Apply (25) to the numerator
bound from (22)--(24), and divide by this determinant to power
2j+1. The result is exactly (7) with (6).

All phases of x0 have been allowed. The nearest-residue choice
in Section 3 varies with that phase but only proves a uniform
inequality; it does not define a new branch of the source.

## 6. Complete meridian, Borel scope, and proof coverage

At x0=-q0^(-1), x0^N is 1 or -1. Since c is even and
Delta(1)=1, d=1 for K={1,-1}. In fact [G] gives D_N=1 for
all tau there. This verifies the complete-point specialization
directly, with every head residue and both quantum-normal
paths retained.

The guaranteed Gevrey type is now C1 N log(eN). Thus the
coefficientwise Borel transform
\[
                    \sum_{j\ge0}V_j(x_0,1)\xi^j/j!
\]
has a guaranteed disk of radius
\[
                            (C_1N\log(eN))^{-1}.              \tag{26}
\]
The numerator bound in (7) gives its usual geometric-series
majorant inside this disk. This is uniform on the prescribed
compact classical-meridian set. By the exact evenness in M
from [G], the fixed-M statement also descends to Y=M^2.
Ordinary meridian derivatives can be bounded on smaller
compacts by Cauchy using a larger compact avoiding the same
Alexander zeros.

The prefactor N^(p+2) exp(ell aN) can still have a positive
exponential rate. The bound does not compare that rate with
volume, supply a nonzero selected geometric component, or
continue the Borel transform beyond its guaranteed local disk.
No Laplace sum, equality to an analytic completion at grading
one, or large-level lower bound follows.

This is a refinement of the explicit same-source bound in
[G]; its broad Gevrey literature coverage remains as recorded
there. No external proof is imported and no novelty claim is
made for general knot-series Gevrey regularity. The sole
complete proof direct is:

| Label | Complete source | SHA256 |
|---|---|---|
| G | notes/research_all_root_verma_gevrey_bound.md | ed6ae262bf5ec44411d7d9f73768011c0ab58fd34f6bf6adc96d46b31f80c776 |

G supplies the literal normalized source, both rational normal
paths, their exact grading-degree bounds, and the determinant
normalization. The root-head, factorial-unit, nearest-cycle,
finite-sector, and moving-circle estimates are proved above.
No mathematical programs, tests, or numerical experiments
are used.

