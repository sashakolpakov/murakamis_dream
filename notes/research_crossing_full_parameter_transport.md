# Transport of the original crossing source in all three boundary parameters

22 November 2026. Written research proof.
Earlier final notes and the frozen manuscripts remain unchanged.

The original crossing polynomial satisfies three first-order equations,
one for each boundary parameter. The coefficients multiplying the
shifted source terms have degree two, independent of the quantum
level. The common inhomogeneous term is explicitly known.
The canonical Gamma product solves the corresponding homogeneous
equations.

These equations extend the proved relative asymptotic to every compact
subset of the positive pair-angle domain. In particular, neither a bound
on the sum of all three angles nor a separate log-sine gap at the target
is necessary. The normalization is still supplied by the earlier
fractional-source theorem on one fixed seed neighborhood. This note
does not replace that theorem by interpolation of its integer samples.

The result concerns the actual crossing source, with its original
closing functional. It does not yet control a general closed Conway
construction or prove the finite-exception theorem.

## 1. Source, canonical section, and the domain

Fix an integer \(N\ge2\), and write
\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad
 \eta=(-1)^d,\qquad \kappa=e^{\pi i d^2/(2N)}.
 \tag{1}
\]
All powers use these exponentials. The complete original source
algebra, its centered basis \(f_0,\ldots,f_d\), and its Frobenius
functional \(\phi\) are those of [P]. In particular
\[
 U_x=\sum_{j=0}^d x^j f_j,\qquad
 \phi(f_i f_j)=\delta_{ij},\qquad f_0f_d=N^{-1}1.
 \tag{2}
\]
For the last identity, [P] gives \(f_0=R^+/\sqrt N\),
\(f_d=R^-/\sqrt N\), and \(R^+R^-=1\). All these identities
hold on the full nonreduced algebra, including its derivative
coordinates at repeated Casimir roots.

The polynomial considered here is
\[
 \Phi_N(C,H,K)=\phi(f_0U_{-C}U_{-H}U_{-K}).
 \tag{3}
\]
It is symmetric and separately of degree at most \(d\). Introduce
marked angles by
\[
 C=e^{-2\pi ic},\qquad H=e^{-2\pi ih},\qquad K=e^{-2\pi ik},
 \qquad
 \varphi_N(c,h,k)=\Phi_N(C,H,K).
 \tag{4}
\]
The polynomial is periodic in the angles. Its canonical Gamma section
need not be periodic.

Write \(\mathfrak F_N\) for the canonical meromorphic factorial of
[G]. The identities used below are
\[
 \mathfrak F_N(r)=(Q;Q)_r\quad(0\le r<N),\qquad
 \mathfrak F_N(w+1)=(1-Q^{w+1})\mathfrak F_N(w).
 \tag{5}
\]
Define the same canonical section as in [G,R]:
\[
 \Gamma_N(c,h,k)=\frac{\kappa^2}{N^2}
 \frac{\displaystyle\prod_{a\in\{c,h,k\}}
           \mathfrak F_N(N(1-a)-\tfrac12)^2}
      {\displaystyle\prod_{\{a,b\}}
           \mathfrak F_N(N(1-a-b))}.
 \tag{6}
\]
Pairs and singles are counted with their labels, even when angles
coincide. The canonical branches and the factors in (6) are fixed;
no periodic multiplier is introduced.

The real domain in the theorem is
\[
 \mathcal D=\{(c,h,k)\in\mathbb R^3:
        c,h,k>0,\quad c+h,c+k,h+k<1\}.
 \tag{7}
\]
It is convex. Its defining inequalities concern pairs, not the sum
of three angles. We will prove that for every compact
\(\mathcal K\subset\mathcal D\), there are \(A,\delta>0\) such that
\[
 \frac{\varphi_N}{\Gamma_N}
       =1+O(N^A e^{-\delta N})
           \quad\hbox{uniformly on }\mathcal K.
 \tag{8}
\]
There is also a fixed complex neighborhood of \(\mathcal K\) on
which the relative error, and each of its fixed-order derivatives,
are exponentially small. Both statements hold along the full sequence
of sufficiently large integer levels.

## 2. The exact three coordinate equations

Let \(\sigma_C\) increase \(c\) by \(1/N\), fixing \(h,k\).
In activities it sends \(C\) to \(C/Q\). Define \(\sigma_H\) and
\(\sigma_K\) by permutation. Put
\[
 J_N(C,H,K)=\frac{\eta}{N}
       [2+C^N+H^N+K^N-(CHK)^N].
 \tag{9}
\]
It is invariant under all three shifts.

**Theorem 1.** As a polynomial identity, at every level \(N\ge2\),
\[
 \boxed{\quad
 (1-C/q)^2\Phi_N(C/Q,H,K)
    -(1-CH)(1-CK)\Phi_N(C,H,K)=C J_N(C,H,K).
 \quad}
 \tag{10}
\]
The other two equations are its permutations. The canonical section
satisfies the corresponding meromorphic homogeneous equation
\[
 \sigma_C\Gamma_N=g_C\Gamma_N,\qquad
       g_C=\frac{(1-CH)(1-CK)}{(1-C/q)^2}.
 \tag{11}
\]

### Proof of the polynomial equation

Only the full-basis identities in [P] are needed. Set
\[
 C_i=q^{-1}Q^{-i},\qquad a_i=(i+1/2)/N,
                  \qquad 0\le i\le d.
\]
Thus \(C_i=e^{-2\pi i a_i}\), \(C_i^N=-1\), and these are
\(N\) distinct activities. The coherent grid in [P, Section 4] gives
\[
 \Phi_N(C_i,C_j,C_k)=\Gamma_N(a_i,a_j,a_k).
 \tag{12}
\]
Its support is exactly \(i+j,i+k,j+k\le d\). On that support its
value is the explicit nonzero factorial product
\[
 \frac{\kappa^2}{N^2}
 \frac{(Q;Q)_{d-i}^2(Q;Q)_{d-j}^2(Q;Q)_{d-k}^2}
      {(Q;Q)_{d-i-j}(Q;Q)_{d-i-k}(Q;Q)_{d-j-k}}.
 \tag{13}
\]
Outside support it is zero. These are coordinates of the entire
Newton basis; (12) is not a quotient by repeated-root directions.

Let \(W\) denote the left side of (10). We first check that it
vanishes at all \(N^3\) grid points. If \(i<d\), then
\(C_i/Q=C_{i+1}\). Where both samples are supported, their ratio
from (13) is (11). If an admissible sample becomes inadmissible,
then \(i+j=d\) or \(i+k=d\). Respectively \(C_iC_j=1\) or
\(C_iC_k=1\), so the coefficient of the current sample also
vanishes. An inadmissible sample cannot become admissible when
\(i\) increases. Finally at \(i=d\), \(C_d=q\), so the coefficient
of the shifted sample is zero. The current sample can be nonzero
only for \(j=k=0\); then \(C_dC_0=1\), killing its coefficient
as well. This includes the cyclic wrap without division by a
vanishing factor.

The leading coefficients of the source are particularly simple.
Using (2),
\[
 [H^d]\Phi_N(C,H,K)
       =\frac{\eta}{N}\sum_{a=0}^d(CK)^a.
 \tag{14}
\]
Indeed extracting \(H^d\) inserts \(\eta f_d\); multiplying by
\(f_0\) leaves \(\eta/N\), and the bilinear duality in (2) gives
the geometric sum. The other two leading coefficients follow by
symmetry. Consequently
\[
 \begin{split}
 [H^N]W&=\frac{\eta C}{N}[1-(CK)^N],\\
 [K^N]W&=\frac{\eta C}{N}[1-(CH)^N],\\
 [C^{N+1}]W&=\frac{\eta}{N}[1-(HK)^N].
 \end{split}
 \tag{15}
\]
For the last equality, the top contribution from the shifted term
is \(q^{-2}Q^{-d}=1\) times the leading coefficient (14) with
\(C\) in place of \(H\). Subtracting the other top contribution
therefore gives \((1-HK)\sum_{a=0}^d(HK)^a\).

The three expressions in (15) are exactly the corresponding
coefficients of \(CJ_N\). Hence \(R=W-CJ_N\) has degrees at
most \((N,N-1,N-1)\) in \((C,H,K)\). Both \(W\) and \(J_N\)
vanish on the full grid. For each fixed \(C=C_i\), interpolation
in \(H,K\) gives \(R(C_i,H,K)=0\) identically. Thus
\[
                         R=(C^N+1)R_0(H,K).
\]
At \(C=0\), both terms defining \(W\) coincide, whereas
\(CJ_N=0\). It follows that \(R_0=0\). This proves (10),
without dividing by a root factorial or assuming any parity of \(N\).

For (11), increasing \(c\) lowers its single factorial argument
by one, giving \((1-C/q)^{-2}\). It also lowers the two pair
arguments containing \(c\), giving \((1-CH)(1-CK)\) from the
denominator of (6). This proves the exact identity from (5).

### Flatness and the retained cyclic norm

Away from denominators, (10) is the affine equation
\[
 \sigma_C\Phi_N=g_C\Phi_N+b_C,\qquad
                   b_C=\frac{CJ_N}{(1-C/q)^2}.
 \tag{16}
\]
The three equations form a flat affine system. More explicitly, put
\[
 \mathcal Y=\begin{pmatrix}\Gamma_N&\Phi_N\\0&1\end{pmatrix}.
\]
Then
\[
 (\sigma_C\mathcal Y)\mathcal Y^{-1}
          =\begin{pmatrix}g_C&b_C\\0&1\end{pmatrix},
 \tag{17}
\]
and similarly in the other coordinates. Commuting the three shifts
proves compatibility; the resulting meromorphic identities extend
after clearing denominators. The two columns in (17) are solution
and source channels over the parameter field. They are not a
two-dimensional replacement of a physical boundary space.

The full norm around the \(C\) cycle is
\[
 M_C=\prod_{r=0}^{N-1}\sigma_C^r g_C
    =\frac{[1-(CH)^N][1-(CK)^N]}{(1+C^N)^2},
 \qquad
 M_C-1=-\frac{N}{\eta}\frac{C^N J_N}{(1+C^N)^2}.
 \tag{18}
\]
These follow from the finite product over the \(N\)-th roots of
unity and direct subtraction. In particular the norm is not set
equal to one. The identities include their zeros and poles as
meromorphic identities. None of the estimates below divides by
\(J_N\), \(1-M_C\), \(1+C^N\), or the numerator factors of
\(M_C\).

## 3. Positive action on the entire pair domain

Define
\[
 L(x)=\int_0^x\log|2\sin\pi t|\,dt,\qquad
 T(a,b)=L(a+b)-L(a)-L(b).
 \tag{19}
\]
For \(a,b>0\), \(a+b<1\), one has \(T(a,b)>0\). To see this,
fix \(s=a+b\in(0,1)\). The function
\(t\mapsto L(s)-L(t)-L(s-t)\) vanishes at the endpoints and has
second derivative
\[
 -\pi\,[\cot\pi t+\cot\pi(s-t)]
     =-\frac{\pi\sin\pi s}{\sin\pi t\sin\pi(s-t)}<0.
 \tag{20}
\]
Strict concavity proves the assertion. Set
\[
 A_0(c,h,k)=T(c,h)+T(c,k)+T(h,k).
 \tag{21}
\]
It is strictly positive on \(\mathcal D\).

The canonical strip expansion proved in [G, Section 3] applies
whenever all singles and pairs have real parts strictly between
zero and one. Applied literally to (6), it gives, uniformly on
compact subsets of the real domain (7),
\[
             \log|\Gamma_N|=N A_0+O(\log N).
 \tag{22}
\]
No factorial argument contains \(1-c-h-k\). Thus (22) requires
no continuation across a factorial singularity when \(c+h+k=1\).
In particular, for every compact \(\mathcal L\subset\mathcal D\),
there are \(a,B>0\) with
\[
          |\Gamma_N|\ge N^{-B}e^{aN}
                          \quad\hbox{on }\mathcal L.
 \tag{23}
\]

For clarity, the full leading expression on this real domain is
\[
 \begin{split}
 \Gamma_N&=\kappa^2N^{-1/2}\mathcal B
                      e^{N\mathcal S}(1+O(N^{-1})),\\
 \mathcal S&=A_0-\pi i(ch+ck+hk),\\
 \mathcal B&=\frac{e^{\pi i(c+h+k)}}
 {2\sqrt{2\sin\pi(c+h)\sin\pi(c+k)\sin\pi(h+k)}}.
 \end{split}
 \tag{24}
\]
All square roots of positive real magnitudes in this display are
positive. One can check the extension of the phase without any
branch inference: for \(0<x<1\), the real part of
\(\operatorname{Li}_2(e^{-2\pi ix})\) is
\(\pi^2(x^2-x+1/6)\), while its imaginary part is \(2\pi L(x)\).
These identities follow from the Fourier series for the dilogarithm
on the unit circle, integrating the log-sine series for the imaginary
part and the linear sine series for the real part.
Substitution in [G, (18)] gives (24). Its amplitude follows from
\(\mathfrak h(1-x)=i e^{-\pi ix/2}\sqrt{2\sin\pi x}\).
Only singles and pairs occur in these checks.

## 4. Propagation from one fixed normalization neighborhood

The sole imported normalization is [R, Section 7]. It supplies (8)
on compact subsets of
\[
 \mathcal U=\{c,h,k>0:\ c+h+k<1,\quad
                  L(c+h+k)-L(h+k)>0\}.
 \tag{25}
\]
There is a fixed neighborhood of
\(b_*=(1/6,1/6,1/6)\) with closure in this region. At \(b_*\)
the gap is \(L(1/2)-L(1/3)>0\). Here \(L(1/2)=0\), and
\(L(x)<0\) for \(0<x<1/2\), as follows from the log-sine
integral and its derivative. Only this fixed neighborhood will
be used; a target need not satisfy (25).

Fix a compact \(\mathcal K\subset\mathcal D\). For a target
\(a=(c,h,k)\in\mathcal K\), select, in each coordinate,
\[
 b_j=\frac16+\frac{\{N(a_j-1/6)\}}{N},
                     \qquad j=1,2,3.
 \tag{26}
\]
Braces denote fractional part in \([0,1)\). Thus
\(b_j\in[1/6,1/6+1/N)\), and \(a_j-b_j\in N^{-1}\mathbb Z\).
For large \(N\), all these seed points lie in one fixed compact
normalization neighborhood from (25).

There is a coordinate path between target and seed using fewer
than \(3N\) steps of size \(1/N\), within one fixed compact
\(\mathcal L\subset\mathcal D\), independent of the target and
large \(N\). A specific construction avoids any discretization
assumption. Starting at the target, first lower every coordinate
that exceeds its seed coordinate. All pair sums then decrease.
Next raise the other coordinates to their seed values. During
this second stage every coordinate is at most its seed value,
so every pair sum is at most \(1/3+2/N\). Throughout both stages,
each coordinate is at least the smaller of its target and seed
values. Compactness of \(\mathcal K\) therefore supplies fixed
strict lower bounds on singles and fixed strict upper bounds
below one on pairs. These bounds define the required compact
\(\mathcal L\). Each coordinate changes by less than one, proving
the step count. Reverse this path to travel from seed to target.

Write
\[
                   E_N=\varphi_N/\Gamma_N-1.
\]
Equations (10)--(11) give the additive, rather than multiplicative,
error equation
\[
 E_N(c+1/N,h,k)-E_N(c,h,k)
  =\frac{C J_N(C,H,K)}
       {(1-C/q)^2\Gamma_N(c+1/N,h,k)}.
 \tag{27}
\]
On the real path, \(|J_N|\le6/N\), and the factor
\(|1-C/q|\) is bounded below uniformly for large \(N\). Indeed
the compact single-angle margins separate \(c+1/(2N)\) from
integers. The other two coordinates have the same bounds.
By (23), every increment in (27) is at most
\(N^B e^{-aN}\), after changing constants. A backward step is
the negative of the forward increment at its lower endpoint;
both endpoints remain on the constructed path.

At the seed the error is \(O(N^{B_0}e^{-a_0N})\) by [R].
Summing fewer than \(3N\) increments proves (8). The proof includes
every fractional class, the half-grid and integer resonances,
both parities, and composite levels. Its denominators are exactly
those displayed in (27), not cyclic-norm factors. This proves
the real assertion without a new fractional initializer or a
second-order recurrence estimate.

## 5. A fixed complex neighborhood and derivatives

We give the complexification argument because small real error
alone is insufficient. Work first over a closed real product box
inside \(\mathcal D\), enlarged slightly while remaining there.
By (8) and the Gamma strip bounds, \(|\Phi_N|\le e^{b_0N}\)
on its activities, after enlarging \(b_0\).

In each real angular interval choose \(d+1\) equally spaced nodes
on an interval of fixed length \(s<1/2\). If their activities are
\(C_j\), then
\[
 \prod_{i\ne j}|C_j-C_i|
   \ge(4s/d)^d j!(d-j)!\ge(2s/e)^d.
 \tag{28}
\]
The first inequality is the elementary chord bound
\(|e^{2\pi ix}-e^{2\pi iy}|\ge4|x-y|\) for
\(|x-y|\le1/2\). For the second use
\(j!(d-j)!\ge d!/2^d\) and \(d!\ge(d/e)^d\).
On a fixed activity disk \(|C|\le B\), each Lagrange numerator
is at most \((1+B)^d\). Interpolation in the three variables
therefore bounds \(|\Phi_N|\) by \(N^3e^{b_1N}\) on every
fixed bounded activity polydisk.

Choose a fixed complex angle box so that the real parts of all
singles and pairs remain strictly between zero and one. On this
box, the canonical strip result in [G] makes \(\Gamma_N\)
holomorphic and nonzero for all large \(N\), and bounds its
reciprocal by \(N^B e^{b_2N}\). Thus \(E_N\) is holomorphic
there with the rough bound \(e^{bN}\). Its real restriction is
bounded by \(e^{-aN}\) for some \(a>0\), absorbing the polynomial
in (8).

Here is the one-variable propagation used in each coordinate.
In a centered upper rectangle \(|x|<R_0\), \(0<y<R_0\), put
\[
 W(x,y)=2y/R_0+(x^2-y^2)/R_0^2.
\]
It is nonnegative on the bottom and at least one on the other
three sides. The maximum-modulus principle applied to
\[
 E_N(z)\exp\{aN-(a+b)N
                         (z^2/R_0^2-2iz/R_0)\}
 \tag{29}
\]
gives \(\log|E_N|\le-aN+(a+b)NW\). Choose a fixed \(r_0>0\)
with
\[
 2r_0/R_0+(r_0/R_0)^2\le a/[2(a+b)].
\]
Then \(|E_N|\le e^{-aN/2}\) on the smaller upper square. The
lower rectangle uses the opposite sign of the linear term in
(29). Apply this in the first coordinate with the others real,
then in the second with the first in its smaller complex box,
then in the third. The rough complex bound is available at
each stage. After shrinking the three radii, the exponent is
at least \(a/8\). All radii are independent of \(N\).

A finite covering of a compact \(\mathcal K\subset\mathcal D\)
proves that there are fixed open complex neighborhoods
\(V'\Subset V\) of \(\mathcal K\) and \(a'>0\) such that
\[
 \sup_V|E_N|=O(e^{-a'N}),\qquad
 \sup_{V'}|\partial^\alpha E_N|
                       =O_\alpha(e^{-a'N})
 \tag{30}
\]
for every fixed multi-index \(\alpha\), by Cauchy's formula.
One may decrease \(a'\) and shrink the neighborhoods to obtain
bounded closures. This does not estimate derivative orders
growing with \(N\), or supply a fixed complex neighborhood at
an endpoint of (7).

Combining (24) and (30) gives the corresponding nonzero leading
asymptotic for the original source, with the same normalization
and phase. The relative Gamma error is exponentially small;
the displayed leading Stirling approximation still has its own
\(O(N^{-1})\) remainder.

## 6. What has been simplified, and what remains

The polynomial equation (10) has degree two in its shift
coefficients, independent of \(N\). After exact Gamma
normalization its propagation is a sum of explicit increments.
The positivity needed for that sum is the elementary concavity
calculation (20). A single fixed normalization neighborhood now
serves the whole real domain (7).

The polynomial degree \(N-1\) of each original boundary variable
has not become bounded. Nor has a physical \(N\)-dimensional
boundary packet been replaced by the affine two-column system
(17). These distinctions matter when applying this result to
the separate fixed-degree auxiliary-error expansion: projecting
that expansion to degree zero retains the actual contraction,
whose lower bound must still be proved.

For general Conway gluing one must still control the actual
inverse pairing, its support, the prescribed ordered turns and
crossings, and the original closing row. Some geometric
continuations have complex heights outside the neighborhood
in (30), or cross a pair-angle strip wall. No assertion about
those continuations follows here. In particular, this theorem
does not prove a nonzero geometric contribution for every fixed
short partial filling. That is still needed for the proposed
finite-exception argument.

The complete direct proof sources are:

| Label | Complete source | SHA-256 |
|---|---|---|
| P | [Exact pairwise source, 668 lines](research_exact_pairwise_conway_source.md) | 470c9df0384274623a1aa0b6939067021894f2fea41595dfa7440081ca77f1d1 |
| G | [Exact Gamma section, 632 lines](research_crossing_exact_gamma_source_extension.md) | f19221b384ae9c2de47beee8460df4eee30f3419df6cf0478c18569b3f464495 |
| R | [Fractional-source rigidity, 705 lines](research_crossing_gamma_fractional_rigidity.md) | dddd36def4235a1cf69703fd886922103e4db2877a5ac68b3a070d31c186bab7 |

All three complete matching sources were read. The new polynomial
equations use the full grid and leading coefficients of [P]. The
canonical strip estimates and normalization in (6) are those of
[G]. Only the seed estimate in Section 4 is imported from [R];
the new propagation and complexification are proved above.
Only written mathematics and text operations were used.
