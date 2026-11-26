# One finite hypergeometric sum for the original multiplication tensor

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The generating polynomial of the centered Conway multiplication
tensor can be recovered from one finite, very-well-poised
\({}_6\phi_5\) partial sum. The original Frobenius source is a
specified first derivative of that sum at the root. The sum itself
vanishes there, so its value cannot replace the derivative.

The proof calibrates a generic-node interpolation at both values
and first derivatives before taking the limit. It does not use
Rogers' infinite summation formula on the unit circle. No geometric
noncancellation or volume bound is claimed.

## 1. The original generating polynomial

Fix \(N\ge2\), and put
\[
 d=N-1,\qquad \eta=(-1)^d,\qquad q=e^{\pi i/N},\quad
 Q=q^2,\quad \kappa=q^{d^2/2},\quad
 c_j=qQ^j+q^{-1}Q^{-j}.
 \tag{1}
\]
Use the full original algebra
\(\mathcal H_N=\mathbb C[z]/P_N(z)\),
\(P_N(z)=2T_N(z/2)+2\), its original Frobenius row \(\phi\),
and its positive crossing \(R\). Here
\(T_N(\cos\theta)=\cos(N\theta)\). The centered compiler supplies
the basis \(f_a=N^{-1/2}R\,p_a(z)\), where \(p_0=1\), and
\[
 \phi(f_af_b)=\delta_{ab},\qquad
 C_{abc}=\phi(f_af_bf_c),\qquad
 G_N(t;z)=\sum_{a=0}^dp_a(z)t^a .
 \tag{2}
\]
The three-boundary polynomial of interest is exactly
\[
 \mathcal C_N(t_1,t_2,t_3)
  =\sum_{a,b,c=0}^dC_{abc}t_1^at_2^bt_3^c
  =N^{-3/2}\phi\!\left(R^3\prod_{\nu=1}^3G_N(t_\nu;z)\right).
 \tag{3}
\]
In particular this uses the original closing, not the bilinear
functional \(\phi(R^2\,\cdot)/N\) with its extra \(R\) omitted.

Here are the complete physical data used from the generating-section
theorem. For \(|t|<1\), set \(D_N(t)=1-\eta t^N\). Then
\[
 G_N(t;c_j)=D_N(t)
 \frac{\displaystyle\prod_{\ell=-j+1}^{0}
                         (1+q^{-1}Q^\ell t)}
 {\displaystyle\prod_{\ell=1}^{j+1}
                         (1+q^{-1}Q^\ell t)} .
 \tag{4}
\]
Empty products equal one. At a double node choose
\(0\le j<d/2\), and write
\[
 s_j=qQ^j-q^{-1}Q^{-j},\qquad
 F_\ell(t)=\frac{q^{-1}Q^\ell t}{1+q^{-1}Q^\ell t}.
 \tag{5}
\]
All \(s_j\) in this range are nonzero. The actual first derivative
has the equivalent finite form
\[
 \frac{\partial_zG_N(t;c_j)}{G_N(t;c_j)}
                   =\frac1{s_j}\sum_{\ell=j+2}^{N-j}F_\ell(t).
 \tag{6}
\]
For clarity, (6) includes the central correction in the initialized
root equation. Indeed its weighted-primitive form is
\[
 \frac1N\sum_{k=0}^d
       \frac{kQ^{-k}t}{1+c_jQ^{-k}t+Q^{-2k}t^2}
 -\frac{\eta(d-2j)}{s_j}\frac{t^N}{D_N(t)} .
 \tag{7}
\]
Partial fractions turn the first term into
\[
 \frac1{Ns_j}\sum_{k=0}^dk
                   \{F_{j+1-k}(t)-F_{-j-k}(t)\}.
 \tag{8}
\]
All indices here are cyclic modulo \(N\). Reindexing gives
\[
 \frac1{s_j}\left\{
   \sum_{\ell=j+2}^{N-j}F_\ell
      -\frac{d-2j}{N}\sum_{\ell=1}^{N}F_\ell\right\}.
 \tag{9}
\]
The full cyclic sum is
\(\sum_{\ell=1}^{N}F_\ell=-\eta Nt^N/D_N(t)\).
Thus the last term of (9) cancels the second term of (7),
proving (6). Dropping that central term would give the wrong
Hermite data. At odd \(N\), the simple node \(-2\) needs only
the value in (4).

## 2. Generic finite products recover the whole Hermite class

Keep \(N\) fixed and let \(\xi\) vary near \(q\). Write
\[
 Q_\xi=\xi^2,\quad
 c_j(\xi)=\xi Q_\xi^j+\xi^{-1}Q_\xi^{-j},\quad
 \kappa_\xi=\xi^{d^2/2},\quad
 \omega_j(\xi)=\kappa_\xi(-1)^j\xi^{j(j+1)} .
 \tag{10}
\]
A fixed holomorphic branch of the power defines \(\kappa_\xi\).
Introduce the finite products
\[
 H_j(\xi;t)=
  \bigl[1-(-\xi t)^N\bigr]\,
 \frac{\displaystyle\prod_{\ell=-j+1}^{0}
                    (1+\xi^{-1}Q_\xi^\ell t)}
 {\displaystyle\prod_{\ell=1}^{j+1}
                    (1+\xi^{-1}Q_\xi^\ell t)} .
 \tag{11}
\]
For fixed \(N\), these are holomorphic for \(\xi\) sufficiently
near \(q\) and \(t\) in any fixed closed disk inside the unit disk.

For generic \(\xi\), interpolate the \(N\) values \(H_j(\xi;t)\)
at the distinct nodes \(c_j(\xi)\) by a polynomial
\(\widetilde G_\xi(t;z)\) of degree below \(N\).
Likewise interpolate \(\omega_j(\xi)\) by
\(\widetilde R_\xi(z)\).

**Lemma 1.** Both polynomial families extend holomorphically to
\(\xi=q\), and
\[
                 \widetilde G_q(t;z)=G_N(t;z),\qquad
                 \widetilde R_q(z)=R(z)
                         \quad\hbox{in }\mathcal H_N .
 \tag{12}
\]

**Proof.** The only coincident nodes at \(q\) are the pairs
\(j,k=d-j\). Their differences have nonzero first derivative:
with a dot denoting \(\xi\partial_\xi\),
\[
                     \dot c_j(q)-\dot c_k(q)=2Ns_j .
 \tag{13}
\]
The two values in each pair agree at the root. For \(H_j\)
this follows from (4); for \(\omega_j\) it follows directly
from (10). Thus all corresponding divided differences have
removable singularities. Grouping each pair in Lagrange
interpolation proves regularity of the coefficients. Equivalently,
one may use Newton interpolation with each coalescing pair adjacent:
the only vanishing denominator is its simple difference (13).

It remains to check which Hermite polynomial these limits give.
The common scalar in (11) cancels from a difference of logarithmic
derivatives. For \(k=d-j\), the extra numerator indices of \(H_k\)
are \(-k+1,\ldots,-j\); adding \(N\) identifies them with the
extra denominator indices \(j+2,\ldots,N-j\).
Their powers have logarithmic derivatives differing by \(2N\).
Consequently
\[
 \frac{\dot H_j(q;t)-\dot H_k(q;t)}{H_j(q;t)}
                 =2N\sum_{\ell=j+2}^{N-j}F_\ell(t).
 \tag{14}
\]
Dividing by (13) gives exactly (6). Together with (4),
this proves the first equality in (12), including every
double-node derivative.

The original crossing has the nodal values
\[
 R(c_j)=\omega_j(q),\qquad
 \frac{R'(c_j)}{R(c_j)}
                         =\frac{2j-d}{2s_j}
 \tag{15}
\]
at the paired nodes. From (10),
\[
 \frac{\dot\omega_j(q)-\dot\omega_k(q)}{\omega_j(q)}
             =j(j+1)-k(k+1)=N(2j-d).
 \tag{16}
\]
Equations (13) and (16) reproduce (15). Simple nodes require
only their value. Full Hermite uniqueness proves the second
equality in (12). \(\square\)

These interpolating families are auxiliary. No claim is made that
their off-root values equal an independently chosen moving-meridian
or generic quantum-group source. Their entire root Hermite limits
have been checked, which is what (3) needs.

## 3. A weighted node limit is the original Frobenius source

Write
\[
 [m]_\xi=\frac{\xi^m-\xi^{-m}}{\xi-\xi^{-1}},\qquad
 \mathcal L_\xi(f)=
       \frac{\eta}{[N]_\xi}
          \sum_{j=0}^d[2j+1]_\xi f(c_j(\xi)).
 \tag{17}
\]

**Lemma 2.** If the coefficients of a polynomial family \(f_\xi\)
are holomorphic near \(q\), then
\[
                         \lim_{\xi\to q}\mathcal L_\xi(f_\xi)
                                     =\phi(f_q).
 \tag{18}
\]
Its degree may exceed \(N-1\); the right side uses the original
class modulo \(P_N\).

**Proof.** In each pair \(j,k=d-j\), the root weights have opposite
signs and the root nodes agree. The numerator in (17) therefore
vanishes at \(q\). At a possible odd simple node its weight is
\([N]_\xi\). Moreover
\[
                (\xi\partial_\xi)[N]_\xi\big|_{\xi=q}
                         =-\frac{2N}{q-q^{-1}} .
 \tag{19}
\]
For a pair with common root \(c\), direct differentiation of
the numerator and division by (19) gives
\[
                  (-1)^N\{c f_q(c)+(c^2-4)f_q'(c)\}.
 \tag{20}
\]
Terms differentiating the coefficients of \(f_\xi\) cancel
between the opposite root weights. At odd \(N\), the simple
node contributes \(f_q(-2)\).

Here is an independent check that this is exactly \(\phi\).
The leading coefficient of \(e_d\) is \(\eta/N^2\), so (3)
of the centered compiler gives
\[
 \phi(f)=\frac{\eta N^2}{2\pi i}
                  \oint_\Gamma\frac{f(z)}{P_N(z)}\,dz ,
 \tag{21}
\]
where \(\Gamma\) is positively oriented and encircles every root
once and no other pole.
Polynomial division justifies (21) at every degree.
The Chebyshev equation is
\[
       (4-z^2)P_N''-zP_N'+N^2(P_N-2)=0.
 \tag{22}
\]
At a double root \(c\), it and its derivative give
\[
 P_N''(c)=\frac{2N^2}{4-c^2},\qquad
 P_N'''(c)=\frac{3cP_N''(c)}{4-c^2}.
 \tag{23}
\]
The residue in (21) is therefore (20).
At the odd simple root \(P_N'(-2)=N^2\), giving \(f(-2)\).
This proves (18). \(\square\)

The derivative in this lemma is a calibrated way of taking the
confluent source. It is not inferred from the nodal values alone.

## 4. The initialized finite \({}_6\phi_5\) sum

For a nonnegative integer \(j\), write
\((a;B)_j=\prod_{h=0}^{j-1}(1-aB^h)\).
Define the following finite sum, with \(Q_\xi=\xi^2\):
\[
 \begin{aligned}
 S_N(\xi;\mathbf t)=
 \sum_{j=0}^d&
 \frac{1-Q_\xi^{2j+1}}{1-Q_\xi}\,
 \frac{\prod_{\nu=1}^3(-\xi/t_\nu;Q_\xi)_j}
      {\prod_{\nu=1}^3(-\xi^3t_\nu;Q_\xi)_j}
                      (-\xi t_1t_2t_3)^j .
 \end{aligned}
 \tag{24}
\]
At zero boundary parameters, use its equivalent regular definition
\[
 S_N(\xi;\mathbf t)=
 \sum_{j=0}^d
 \frac{1-\xi^{4j+2}}{1-\xi^2}\,
 (-\xi)^j
 \frac{\displaystyle\prod_{\nu=1}^3\prod_{h=0}^{j-1}
                       (t_\nu+\xi^{2h+1})}
      {\displaystyle\prod_{\nu=1}^3\prod_{h=0}^{j-1}
                       (1+\xi^{2h+3}t_\nu)} .
 \tag{25}
\]
Thus the sum is holomorphic near \(\xi=q\) on every fixed
closed unit subdisk in its three boundary variables.

It is the first \(N\) terms of the canceled very-well-poised
\({}_6\phi_5\) with base \(Q_\xi\), leading parameter
\(a=Q_\xi\), square root \(\sqrt a=\xi\), three other
parameters \(b_\nu=-\xi/t_\nu\), and argument
\(aQ_\xi/(b_1b_2b_3)=-\xi t_1t_2t_3\).
The factors \((a;Q_\xi)_j/(Q_\xi;Q_\xi)_j\) cancel,
and the square-root factors give
\((1-Q_\xi^{2j+1})/(1-Q_\xi)\).
Formula (25), rather than an uncanceled quotient, specifies
every endpoint and both parities.

For the terminology and standard nonterminating series see
[Schlosser (2000), equation (5.2)](https://arxiv.org/pdf/math/0007046).
That infinite summation theorem is not used here. Our finite
window \(0\le j<N\) is prescribed by the original source, not
by an assertion that an infinite series terminates at the root.

**Theorem.** For \(|t_\nu|<1\),
\[
 \boxed{\quad
 \mathcal C_N(\mathbf t)=
 \frac{(-1)^N(q-q^{-1})\kappa^3}{2N^{5/2}}
 \prod_{\nu=1}^3\frac{1-\eta t_\nu^N}{1+qt_\nu}
 \left.(\xi\partial_\xi)S_N(\xi;\mathbf t)\right|_{\xi=q}.
 \quad}
 \tag{26}
\]
In particular all \(C_{abc}\) are recovered by coefficient
extraction from one finite sum and this specified derivative.

**Proof.** Apply Lemmas 1 and 2 to
\(f_\xi=\widetilde R_\xi^3\prod_\nu\widetilde G_\xi(t_\nu;z)\).
This gives
\[
 \mathcal C_N(\mathbf t)
  =\frac{\eta}{N^{3/2}}\lim_{\xi\to q}
   \frac1{[N]_\xi}\sum_{j=0}^d
     [2j+1]_\xi\,\omega_j(\xi)^3
                      \prod_\nu H_j(\xi;t_\nu).
 \tag{27}
\]
Every first derivative in this equation has already been calibrated.

For generic \(\xi\) the sum in (27) is exactly
\[
 \kappa_\xi^3
 \prod_{\nu=1}^3\frac{1-(-\xi t_\nu)^N}{1+\xi t_\nu}
                         S_N(\xi;\mathbf t).
 \tag{28}
\]
To check it, divide its \(j\)-th term by the common \(j=0\)
factor. Use
\[
 [2j+1]_\xi=Q_\xi^{-j}
                   \frac{1-Q_\xi^{2j+1}}{1-Q_\xi},
 \qquad
 \frac{H_j}{H_0}
   =(\xi^{-1}t)^jQ_\xi^{-j(j-1)/2}
                     \frac{(-\xi/t;Q_\xi)_j}
                          {(-\xi^3t;Q_\xi)_j}.
 \tag{29}
\]
The remaining crossing factor is
\((-1)^jQ_\xi^{3j(j+1)/2}\).
Its product with the three factors in (29) and the dimension
factor is precisely (24).

At \(\xi=q\), the \(j\) and \(d-j\) terms of the original
sum in (27) cancel. At odd \(N\), the middle term has weight
\([N]_q=0\). The common factor in (28) is nonzero in the unit
polydisk, so
\[
                              S_N(q;\mathbf t)=0 .
 \tag{30}
\]
Taking the derivative using (19) proves (26). Derivatives of
the common factor in (28) multiply (30) and vanish. Its root
value, including every \(1-\eta t_\nu^N\) and the actual
\(\kappa^3\), remains in (26). \(\square\)

## 5. A reduced vertex on the original coefficient cycle

The scalar factors \(D_N(t_\nu)\) in (26) must remain in the
polynomial identity. There is a separate exact simplification for
the closed-tree coefficient period.

Reverse finite vertex indices, with the corresponding swaps of
the signed inputs and original caps, as in the generating-section
assembly theorem. Every edge then has anti-diagonal contraction.
If \(V_v\) is the generating polynomial of its actual finite
vertex array, the original scalar is
\[
           [\,\prod_e t_e^d\,]\prod_v V_v((t_e)_{e\ni v}).
 \tag{31}
\]
All powers in these vertex polynomials are nonnegative.
On such a trivalent vertex define the analytic Taylor section
\[
 \widehat{\mathcal C}_N(\mathbf t)=
 \frac{(-1)^N(q-q^{-1})\kappa^3}{2N^{5/2}}
 \prod_{\nu=1}^3(1+qt_\nu)^{-1}
 \left.(\xi\partial_\xi)S_N(\xi;\mathbf t)\right|_{\xi=q}.
 \tag{32}
\]
It is regular near the origin by (25), and (26) says exactly
\[
          \mathcal C_N(\mathbf t)
                 =\prod_{\nu=1}^3D_N(t_\nu)\,
                                   \widehat{\mathcal C}_N(\mathbf t).
 \tag{33}
\]
Since \(D_N(t)=1+O(t^N)\), these two sections agree modulo
the ideal generated by \(t_1^N,t_2^N,t_3^N\).
They therefore give the same original coefficient in (31):
after expanding the difference one vertex at a time, each extra
term has degree at least \(N>d\) on some edge, and no other
factor has negative powers to bring it back to degree \(d\).
The coefficient-conjugate vertex has the conjugate Taylor section.

Equivalently, (31) has its prescribed small-circle representation
\[
 \frac1{(2\pi i)^{|E|}}
    \oint\cdots\oint
       \prod_v V_v((t_e)_{e\ni v})\,
                                \prod_e\frac{dt_e}{t_e^N},
 \tag{34}
\]
with all circles sufficiently small and positively oriented.
The replacements (32) preserve this entire period, including its
actual input and closing arrays. Thus every multiplication vertex
can be written using the one finite sum in (25), its specified
normal and the simple factors \((1+qt_\nu)^{-1}\), on the
original Taylor cycle.

This is a statement about these nonnegative auxiliary generating
powers. It is not a rule for deleting a peripheral \(M^N\)
factor, setting a parameter equal to one, reversing an untruncated
Taylor series, or moving the cycle through a singularity.

## 6. What has been simplified

The three-boundary tensor is now a prescribed confluent finite
hypergeometric source. No unknown interpolation coefficient or
choice of cycle has been added. Both the simple node and all
double-node derivatives survive.

The identity is initially proved on the unit polydisk, where every
factor is regular. Since its left side is a polynomial, the full
right side has the corresponding removable extension wherever an
individual displayed denominator vanishes. This does not allow
individual terms, or their derivatives, to be discarded.

Evaluating the sum only at the root would give zero by (30);
it would lose the original source. Replacing it by an infinite
Rogers product would require a separate argument and is not done.
No nonzero leading coefficient, geometric saddle or lower bound
for an arbitrary short component follows from (26) alone.

## Complete proof sources and coverage

All three complete proof texts were read at the matching pins.
The first fixes \(C\), both closures and all phase conventions;
the second supplies the full physical generating section and its
actual first normals; the third supplies the original crossing's
nodal values and derivatives used in (15).

| Source | SHA-256 |
|---|---|
| [Centered original compiler](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| [Full-degree generating section](research_full_degree_centered_generating_section.md) | 6fbef2085aca79503518745a08d3466ec84cd337ec8131944e2aebb9c95c2f6b |
| [Arbitrary-power original source](research_arbitrary_power_source_compilation.md) | 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f |

The existing arbitrary-power representation already retains the
original angle trace, and the centered compiler already gives
the full three-dimensional Fourier tensor. The identity here is
the particular initialized one-sum representation (26), with
its full Hermite calibration and its unchanged coefficient cycle.
No novelty is claimed for very-well-poised series, confluent
interpolation, residues, or the coefficient-ideal argument.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git
operation or earlier-final edit was performed.
