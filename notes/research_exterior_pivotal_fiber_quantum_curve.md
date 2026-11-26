# Actual source clock connections and the exterior pivotal fiber

Private written proof, 19 November 2026.

For any fixed signed braid word, its actual charged anchor polynomial
has an explicit flat rational clock connection, with a cleared finite
coefficient recurrence of width bounded by the incident block count.
After summing the clocks in an alternating diagram, the rightmost
exterior circulation is a specified finite polynomial. Its coefficients obey an
exact clock-difference equation, including the original pivotal charge.
Both ends of the physical interval annihilate the apparent boundary
sources. This is a reduction of the actual capped source, with arbitrary
remaining charges, rather than an infinite-series replacement.

The complete directs are G for the arbitrary-word charged source and C
for its alternating specialization. All further algebra is proved below.
The term quantum curve refers here only to the displayed finite
difference operator and its commuting
symbol. No knot character curve, geometric cycle, or nonzero closing
value is inferred.

## 0. The arbitrary signed word at fixed bridge clocks

G supplies, with precisely the original averaged cut, pivotal closure
and external scalar, the exact finite identity
\[
 K_N=\frac{\chi_N}{N}\sum_h W_h
               [X_1^d\cdots X_m^d]P_h(X),\qquad d=N-1.
 \tag{G1}
\]
Here h ranges over the literal finite monotone overbridge clocks,
m is the number of retained anchor events, and every scalar crossing,
propagated-frame and closure factor remains in \(W_h\). For each h,
\(P_h\) is a product of blocks
\[
 \mathcal B_{ij,L}(X)=
           \prod_{r=0}^{L-1}(\alpha X_i-Q^r\beta X_j),
                   \qquad 0\le L\le d,\quad Q=e^{2\pi i/N}.
 \tag{G2}
\]
The constants are G's actual nonzero propagated clock factors.
The closure blocks, including their initial Q and pivot, are of this
same form after retaining that factor in beta. All polynomial powers
are nonnegative and \(P_h\) is homogeneous of total degree md,
with zero sectors allowed. G proves that (G1) has no cyclic
anchor aliases; we use that complete source identity unchanged.

Let \(\mathsf T_i\) scale only \(X_i\) by Q. For a nonloop block
with tail X and head Y, direct cancellation of the finite products
gives the following two ratios:
\[
 \begin{split}
 \frac{\mathcal B(QX,Y)}{\mathcal B(X,Y)}
   &=Q^L\frac{\alpha X-Q^{-1}\beta Y}
                    {\alpha X-Q^{L-1}\beta Y},\\
 \frac{\mathcal B(Y,QX)}{\mathcal B(Y,X)}
   &=\frac{\alpha Y-Q^L\beta X}{\alpha Y-\beta X}.
 \end{split}                                                   \tag{G3}
\]
The notation in the second line makes X the head variable.
Length-zero blocks are omitted. If both endpoints are the same
anchor X, its block is a constant times \(X^L\), and its scaling
factor is exactly \(Q^L\). Any separately extracted monomial has
its corresponding factor \(Q^{\deg_X}\).

Multiplying (G3) over the incident blocks therefore gives explicit
polynomials \(A_i(X),B_i(X)\), of degree in \(X_i\) at most the
number of its incident nonloop blocks, for which
\[
                   A_i(X)\mathsf T_iP_h(X)=B_i(X)P_h(X).
 \tag{G4}
\]
The known scalar factors from loops and monomials are included in
\(B_i\). This is a polynomial identity at every assignment of the
remaining variables. In particular it remains true when a block
vanishes, or even when \(P_h\) is identically zero for that h.

On a nonzero polynomial sector define \(r_i=B_i/A_i\) in the
rational function field. There it equals \(\mathsf T_iP_h/P_h\),
so commuting the shifts and using \(Q^N=1\) proves
\[
        (\mathsf T_j r_i)r_j=(\mathsf T_i r_j)r_i,
        \qquad \prod_{s=0}^{N-1}\mathsf T_i^s r_i=1.
 \tag{G5}
\]
These are rational identities, including removable cancellations;
they do not assert invertibility at the zeros of a block. For the
full Laurent coefficient integrand, the extra \(X_i^{-d}\) changes
\(r_i\) to \(Q^{-d}r_i\); flatness and its orbit product one remain.

Finally write, in the variable \(X_i\) alone,
\[
 P_h=\sum_n p_nX_i^n,\qquad A_i=\sum_j A_{i,j}X_i^j,
                         \qquad B_i=\sum_j B_{i,j}X_i^j.
\]
All coefficients here are polynomials in the other anchors. Equation
(G4) is exactly the finite recurrence
\[
          \sum_j\bigl(Q^{n-j}A_{i,j}-B_{i,j}\bigr)p_{n-j}=0
                                      \qquad\text{for every }n.
 \tag{G6}
\]
Missing coefficients, including those outside the actual degree of
\(P_h\), are zero. Thus both the degree cap and all endpoint equations
are retained. Its width is bounded by the incident block count of the
fixed word, independently of N. No division by a coefficient is needed.

This gives an arbitrary-word source connection before the finite
h-sum in (G1). Its coefficients depend on h; a common first-order
connection after that sum is not claimed. Neither (G5) nor (G6)
proves nonvanishing of a prescribed coefficient. The following
alternating reduction instead performs the overclock sums first
and gives a single finite equation on each actual pivotal fiber.

## 1. Original source and the exterior fiber partition

Use
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad x=-q^{-1},\quad s=x^N,
 \quad S_n=\prod_{j=1}^n2\sin(\pi j/N).
 \tag{1}
\]
Thus \(S_0=1\) and \(S_nS_{d-n}=N\). Fix an actual connected
alternating closed-braid diagram with b heads and c crossing
occurrences. Here \(b\ge2\), \(c\ge1\). The crossing signs are
\(\sigma_j\), and \(w=\sum_j\sigma_j\).

C gives the exact source
\[
 \begin{split}
 K_N&=\mathcal C_N\sum_{(u,z)\in\mathcal Q_N}T(u,z),\\
 \mathcal C_N&=\chi_N\kappa^w(x/s)^{b-1}N^{2c-1},\\
 T(u,z)&=
 q^{\frac12\sum_j\sigma_j[(z_j-u_j)(B_j-A_j)-d(u_j+z_j)]
                  -2\tau_{\rm piv}(u,z)}
       \prod_j(S_{u_j}^2S_{z_j}^2S_{d-u_j-z_j})^{-1}.
 \end{split}                                                   \tag{2}
\]
Here \(A_j=u_{a(j)}\), \(B_j=z_{b(j)}\), with C's two port
permutations a and b. The exact integer support is
\[
 \mathcal Q_N=\{u,z\ge0: u_j+z_j\le d,
                         \ u_j+z_j=A_j+B_j\ \text{for all }j\}.
 \tag{3}
\]
The scalar \(\chi_N\), crossing normalizers \(\kappa^{\sigma_j}\),
original framing convention and all original closing pivots remain
exactly those of C. In particular only head 1 is unpivoted.
We do not replace this source by a second fixed physical cut.

Let I be the occurrences of the rightmost generator
\(\sigma_{b-1}^{\pm1}\), and put \(k=|I|\). Connectedness implies
\(k\ge1\). Between successive such occurrences the braid position b
is untouched, including its actual closing arc. At a positive
occurrence its outer input is under and its outer output is over;
at a negative occurrence these are reversed. Alternation forces all
occurrences in I to have the same sign, denoted \(\varepsilon\).

For \(\varepsilon=+1\), the rightmost edge goes from an over-output
to the next under-input. Thus C's b-permutation cycles I. Increasing
all \(z_i\), \(i\in I\), by one increases exactly the corresponding
\(B_i\) by one and preserves every equality in (3).
For \(\varepsilon=-1\), the rightmost edge goes from an under-output
to the next over-input. The a-permutation cycles I; increasing all
\(u_i\), \(i\in I\), by one increases exactly their \(A_i\).
These two increasing directions are used below, regardless of the
direction of a possible complex radial deformation.

Partition \(\mathcal Q_N\) into equivalence classes under this integer
translation. In each class subtract the minimum of the moving charges.
The resulting unique representative has the form
\[
 \begin{array}{c|cc}
 &\text{fixed charge at }i&\text{moving charge at }i\\ \hline
 \varepsilon=+1&u_i=a_i&z_i=b_i+l\\
 \varepsilon=-1&z_i=a_i&u_i=b_i+l
 \end{array}
 \qquad \min_{i\in I}b_i=0.
 \tag{4}
\]
All \(a_i,b_i\) are nonnegative integers. Every charge not listed as
moving is fixed. All conservation equations are already satisfied by
the representative and remain so for every l. The complete physical
fiber is precisely
\[
             0\le l\le K,\qquad
             K=\min_{i\in I}(d-a_i-b_i).
 \tag{5}
\]
In particular it is a consecutive interval, \(0\le K\le d\).
There is no congruence quotient or omitted intermediate cap.
Let \(\mathfrak B_N\) denote these finitely many representatives.

For \(\gamma\in\mathfrak B_N\), let \(T_{\gamma,l}\) be the
literal value of (2) at its l-th state, with the global scalar
\(\mathcal C_N\) excluded. Define its polynomial and its clock shift by
\[
 F_\gamma(t)=\sum_{l=0}^{K}T_{\gamma,l}t^l,
 \qquad (\mathsf T f)(t)=f(Qt).
 \tag{6}
\]
Every \(T_{\gamma,l}\) is nonzero, since all sine factorials in (2)
have indices between zero and d. The original closing is exactly
\[
                       K_N=\mathcal C_N
                                  \sum_{\gamma\in\mathfrak B_N}F_\gamma(1).
 \tag{7}
\]
The identity retains the full exterior and the original pivot; it
does not assert that any summand on the right is nonzero.

## 2. The two literal coefficient ratios

The rightmost closure is one of the pivoted heads. For the positive
fiber its closing charge is B, before the underpass, and increases
by l. For the negative fiber it is \(d-A\), after the underpass,
and decreases by l. No other original closing charge changes:
the flow just constructed is supported on braid position b.
Consequently
\[
 \tau_{{\rm piv},l}=\tau_{{\rm piv},0}+l\quad(\varepsilon=+1),
 \qquad
 \tau_{{\rm piv},l}=\tau_{{\rm piv},0}-l\quad(\varepsilon=-1).
 \tag{8}
\]
Thus their exact pivotal ratios are \(Q^{-1}\) and Q, respectively.

Put
\[
 \alpha_i=Q^{a_i+b_i},\qquad \beta_i=Q^{b_i},\qquad
 c_+=(-1)^k Q^{k-1-\sum_i a_i+\sum_i b_i}
        =(-1)^kQ^{k-1}\prod_i\beta_i^2/\alpha_i.
 \tag{9}
\]
These Greek letters are scalar clock parameters, not C's port
charges \(A_i,B_i\). For every \(0\le l<K\), the actual ratios are
\[
 \boxed{\quad
 \frac{T_{\gamma,l+1}}{T_{\gamma,l}}
  =\begin{cases}
  c_+ Q^{kl}\displaystyle\prod_{i\in I}
       \frac{1-\alpha_iQ^{l+1}}{(1-\beta_iQ^{l+1})^2},
                                      &\varepsilon=+1,\\[2mm]
  Q\displaystyle\prod_{i\in I}
       \frac{1-\alpha_iQ^{l+1}}{(1-\beta_iQ^{l+1})^2},
                                      &\varepsilon=-1.
  \end{cases}\quad}
 \tag{10}
\]

Here is the complete phase calculation. Reflect the last sine
factorial using
\[
 (S_{a_i}^2S_{b_i+l}^2S_{d-a_i-b_i-l})^{-1}
       =\frac{S_{a_i+b_i+l}}{N S_{a_i}^2S_{b_i+l}^2}.
 \tag{11}
\]
Its ratio under \(l\mapsto l+1\), writing \(v_i=b_i+l\), is
\[
 -i q^{v_i-a_i+1}
       \frac{1-Q^{a_i+v_i+1}}{(1-Q^{v_i+1})^2},
 \tag{12}
\]
because \(2\sin(\pi n/N)=i q^{-n}(1-Q^n)\).

In the positive fiber, \(\sum_{i\in I}B_i=\sum_{i\in I}z_i\),
and conservation gives \(\sum A_i=\sum u_i\), even if some A
ports lie outside I. The increment of the half-clock exponent in
(2), before the pivot, is therefore
\[
                 \sum_i v_i-\sum_i a_i+k(1-d)/2.
 \tag{13}
\]
Multiplying its q-power with all factors in (12) gives
\((-1)^kQ^{k+\sum v_i-\sum a_i}\), since \(d=N-1\).
The remaining \(Q^{-1}\) in (8) proves the first line of (10).

For the negative fiber, exchange the moving/fixed roles of u,z
and the corresponding A,B ports. The two factors in
\((z-u)(B-A)\) both change sign, so that product is unchanged.
The negative crossing sign makes (13) its negative. Its q-power
and the phases in (12) cancel exactly:
\[
                    (-i)^k q^{kN/2}=1.
 \tag{14}
\]
Only the pivotal ratio Q remains, proving the second line.
All unchanged factorials and all unchanged source phases cancel in
this ratio calculation, rather than being reset or removed.

Equivalently the complete finite coefficient formula is
\[
 \frac{T_{\gamma,l}}{T_{\gamma,0}}=
 \begin{cases}
 c_+^l Q^{k l(l-1)/2}\displaystyle\prod_i
       \frac{(Q\alpha_i;Q)_l}{(Q\beta_i;Q)_l^2},&\varepsilon=+1,\\[2mm]
 Q^l\displaystyle\prod_i
       \frac{(Q\alpha_i;Q)_l}{(Q\beta_i;Q)_l^2},&\varepsilon=-1.
 \end{cases}
 \tag{15}
\]
It is used only for \(0\le l\le K\). Every denominator factor
there has exponent \(1\le b_i+j\le d\) and is nonzero.

## 3. The finite homogeneous annihilator and its two endpoints

Define polynomials in one commuting letter y by
\[
 P(y)=\prod_i(1-\beta_i y)^2,
 \qquad R(y)=\prod_i(1-Q\alpha_i y).
 \tag{16}
\]
The original polynomial (6) satisfies the exact operator identity
\[
 \boxed{\quad
 \begin{cases}
 [P(\mathsf T)-c_+t\,\mathsf T^k R(\mathsf T)]F_\gamma=0,
                                           &\varepsilon=+1,\\
 [P(\mathsf T)-Qt\,R(\mathsf T)]F_\gamma=0,
                                           &\varepsilon=-1.
 \end{cases}\quad}
 \tag{17}
\]
Multiplication by t is on the left as displayed. In particular
\(\mathsf Tt=Qt\mathsf T\); its placement is part of the formula.

For coefficients \(1\le l\le K\), (17) is exactly (10): its
positive right side is
\(c_+Q^{k(l-1)}R(Q^{l-1})T_{\gamma,l-1}\), and the negative
right side is \(Q R(Q^{l-1})T_{\gamma,l-1}\).
At l=0 the left coefficient is zero since some \(b_i=0\), so
\(P(1)=0\). At l=K+1 the right coefficient is zero since some
\(a_i+b_i+K=d\), so
\[
                  R(Q^K)=0
                  \quad\text{through the factor }1-Q^N.
 \tag{18}
\]
All higher coefficients are zero on both sides. This proves (17)
as an identity of actual finite polynomials, including K=0.
No endpoint source has been discarded and no infinite tail is used.

Conversely, in the space of polynomials of degree at most K, (17)
and the literal value \(F_\gamma(0)=T_{\gamma,0}\) determine
\(F_\gamma\) uniquely. Indeed
\[
                P(Q^l)\ne0\qquad(1\le l\le K),
 \tag{19}
\]
by the same physical denominator bound as for (15). Its coefficients
are therefore determined successively, and (18) supplies the top
compatibility. This uniqueness is asserted only in the stated
physical polynomial space, not among arbitrary cyclic or meromorphic
solutions of a difference equation.

Equations (7) and (17) are a source-compatible finite clock Ward
relation. For example \(F_\gamma(Q^j)\) is the same fiber with the
literal character \(Q^{jl}\) inserted; \((t\partial_t)^nF_\gamma(1)\)
inserts its physical occupation moment \(l^n\). These are not
meridian derivatives. Nor does first-cut scalarity permit replacing
the pivotal evaluation t=1 by arbitrary t. The parameters
\(\alpha_i,\beta_i,c_+\)
depend on the remaining charges. Accordingly one must retain (17)
fiberwise, or as a diagonal-coefficient operator on their direct sum,
before performing (7). A common scalar annihilator for the fully
summed source is not asserted by suppressing that dependence.

## 4. The algebraic symbol and what it does not establish

There is an unambiguous algebraic symbol for this finite row. At finite
N, simply treating t and y as commuting letters in the displayed
ordering gives
\[
 D_+(t,y)=P(y)-c_+t y^kR(y),\qquad
 D_-(t,y)=P(y)-QtR(y).
 \tag{20a}
\]
For a sequence of actual fibers with fixed k, suppose
\(a_i/N\to a_i^*\) and \(b_i/N\to b_i^*\). Write
\[
 A_i^*=e^{2\pi i(a_i^*+b_i^*)},\qquad
 B_i^*=e^{2\pi i b_i^*},\qquad
 c_* =(-1)^k e^{2\pi i\sum_i(b_i^*-a_i^*)}.
 \tag{20}
\]
Replacing the shift by a commuting letter y and taking the
coefficient limit in the displayed ordering gives
\[
 \begin{split}
 \mathscr P_+(t,y)&=
       \prod_i(1-B_i^*y)^2-c_*t y^k\prod_i(1-A_i^*y),\\
 \mathscr P_-(t,y)&=
       \prod_i(1-B_i^*y)^2-t\prod_i(1-A_i^*y).
 \end{split}                                                   \tag{21}
\]
This is only an algebraic object attached to the actual finite row.
No exponential ansatz for \(F_\gamma\), selection of a branch of
(21), or identification with a knot A-polynomial was used to derive
it. In particular (19) does not prove that \(F_\gamma(1)\ne0\).

The result applies to every rightmost exterior circuit in the stated
diagram class, with arbitrary remaining admissible charges and with
the original scalar (2). It requires neither a new knot case nor a
positivity assumption. It does not eliminate the remaining exterior
contraction, prove a geometric period coefficient, or transport a
contour through a cap or an alias without its current. The pivotal
characters in (8), the finite support (5), and the source evaluation
(7) remain part of any subsequent analytic use.

## Complete direct sources

G: notes/actual_global_charged_bridge_flow.md,
354 lines, SHA256
b444e487eab3ec0a56c40b22584837cefcbe374a137b0beeaa185116c2a81d8c.
Its entire arbitrary-word coefficient source is used in Section 0.

C: notes/research_alternating_charged_checkerboard_polarization.md,
435 lines, SHA256
c7102909f30c008e45a8e7040a225f1de4164187709c5548ff316d49954f1098.
The entire original source, its port order and its closing-charge rule
are used above. All finite difference and endpoint arguments are inline.
