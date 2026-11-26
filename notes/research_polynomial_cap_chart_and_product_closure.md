# An exact polynomial cap chart and the limit of product closure

Research note, 3 November 2026. Frozen manuscripts are unchanged.

There is an explicitly normalized hypergeometric input family for the
original step \(A=JM\). Its apparent zero-times-pole ambiguity at the cap
disappears in polynomial coordinates. The resulting identity transports
the actual cap and all its parameter derivatives, with a known monomial
scalar. It does not close a general rational word under \(M,J\).

The latter limitation can be made precise for one proposed algorithm:
an exact family made from a bounded number of factorial/Pochhammer
factors, with bounded-degree rational \(Q\)-shift ratios, already fails
for the canonical three-crossing source. Its required rational shift
ratio has degree at least \(N-2\). This does not obstruct a fixed-channel
forced system or an asymptotic factorial profile.

## 1. The original finite transform

Put \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(\kappa=q^{D^2/2}\), using the displayed logarithm. Write
\[
 (a;Q)_k=\prod_{r=0}^{k-1}(1-aQ^r),\qquad
 M_{jk}=\kappa(-q)^j q^{k^2}{j\brack k}_Q
 \quad(0\le k\le j<N),\qquad
 (Jh)_j=h_{D-j}.
 \tag{1}
\]
These are the full original Newton matrices, including their endpoint
rows and the repeated-root algebra. The Gaussian binomials in (1)
have no zero denominator because every factorial index is below \(N\).

Initially at generic nonzero \(a,b\), define
\[
 f_k(a,b)=\frac{(a;Q)_k}{(b;Q)_k}
                 \left(-\frac b{qa}\right)^k .
 \tag{2}
\]
The finite Chu--Vandermonde identity gives
\[
 (Mf(a,b))_j
       =\kappa(-q)^j\frac{(b/a;Q)_j}{(b;Q)_j}.
 \tag{3}
\]
For precision, the identity being used is
\[
 \sum_{k=0}^{j}
 \frac{(Q^{-j};Q)_k(a;Q)_k}
      {(Q;Q)_k(b;Q)_k}
       \left(\frac{bQ^j}{a}\right)^k
       =\frac{(b/a;Q)_j}{(b;Q)_j}.
 \tag{4}
\]
Substitute
\({j\brack k}_Q=(-1)^kQ^{jk-k(k-1)/2}
(Q^{-j};Q)_k/(Q;Q)_k\) in (1) to obtain (3).
An independent finite telescoping proof of (4), before root
specialization, is in the appendix of
[the adjacent-source normal form](adjacent_source_normal_form.md).
This is the classical
[first \(q\)-Chu--Vandermonde sum, DLMF 17.6.2](https://dlmf.nist.gov/17.6.E2);
no new summation formula is asserted.

The exact reversal identity required here is
\[
 (a;Q)_{D-k}
 =\frac{(a;Q)_D}
 {(-a)^kQ^{kD-k(k+1)/2}(Q^{\,1-D}/a;Q)_k},
 \qquad Q^{\,1-D}=Q^2.
 \tag{5}
\]
The shift is \(Q^2\), rather than \(Q\). It uses the literal last
index \(D=N-1\).

## 2. Polynomial coordinates retain the cap

Clear the denominators in (2) by setting
\[
 w_k(a,b)=
 a^{D-k}b^k(-q^{-1})^k
       (a;Q)_k(bQ^k;Q)_{D-k},
 \qquad 0\le k\le D.
 \tag{6}
\]
Thus \(w=a^D(b;Q)_D f\) on the generic set, but (6) is the definition
at its divisors. The vector is polynomial in \(a,b\).
Define
\[
 T(a,b)=\left(\frac{Q^2}{b},\frac{Q^2a}{b}\right),
 \qquad
 \lambda_N(a,b)=\kappa q^{D(D-4)}b^{2D}.
 \tag{7}
\]

**Theorem 1.** On \((\mathbb C^*)^2\), as an identity of actual
finite coefficient vectors,
\[
 \boxed{\quad (JM)w(a,b)=\lambda_N(a,b)\,w(T(a,b)).\quad}
 \tag{8}
\]
The scalar is a nonzero monomial. The cap orbit consists of three
regular vectors:
\[
 \begin{array}{c|c}
 (a,b)&w(a,b)\\ \hline
 (1,Q)&N\mathbf e_0\\
 (Q,Q)&NQ^D\bigl((-q^{-1})^k\bigr)_{k=0}^D\\
 (Q,Q^2)&N(-q^3)^D\mathbf e_D .
 \end{array}
 \tag{9}
\]
In particular (8) is regular in a neighborhood of each of these
points. It retains parameter jets there, and evaluation of the
resulting Newton polynomial retains every ordinary boundary normal.

*Proof.* Equations (3) and (5), on their generic domain, give
\[
 (JM)f(a,b)
 =\kappa(-q)^D\frac{(b/a;Q)_D}{(b;Q)_D}\,
                     f(T(a,b)).
 \tag{10}
\]
The full-product reversal is
\[
 (b/a;Q)_D
   =(-b/a)^D Q^{D(D-1)/2}(Q^2a/b;Q)_D.
 \tag{11}
\]
Multiplying (10) by \(a^D(b;Q)_D\), and using (11), gives (8):
the constant is
\(\kappa q^D Q^{D(D-5)/2}b^{2D}
=\kappa q^{D(D-4)}b^{2D}\).
This argument took place in a rational function field. Clearing
the remaining monomials gives a polynomial identity, so (8)
continues to every nonzero \(a,b\), including the cap orbit.

At \((1,Q)\), the numerator \((1;Q)_k\) kills every \(k>0\),
and \((Q;Q)_D=N\). At \((Q,Q)\), the two products in (6)
join to \((Q;Q)_D\). At \((Q,Q^2)\), the second product
contains \(1-Q^N\) whenever \(k<D\); for \(k=D\) it is
empty. These observations prove (9). A displayed nonzero
component remains nonzero on a neighborhood of each point.
Finally (8) is an identity in the original coefficient space:
pairing it with \((e_0(z),\ldots,e_D(z))\) and differentiating
preserves the full ordinary polynomial, including first normals
at double physical roots. \(\square\)

There is no globally nonvanishing-vector assertion for (6);
other parameter points can be base points. Nor are \(a,b\)
being identified with geometric meridians.

For a normalization check, \(T^3=\mathrm{id}\), and
\[
 \lambda_N(a,b)\lambda_N(T(a,b))\lambda_N(T^2(a,b))
     =\kappa.
 \tag{12}
\]
Indeed the product of the three second parameters is \(Q^4\);
the left side is
\(\kappa^3q^{3D^2+4D}=\kappa\), since
\(\kappa^2=q^{D^2}\) and \(q^{4D(D+1)}=1\).
Thus the chart is consistent with the original braid identity
\((JM)^3=\kappa I\). Directly at the cap,
\[
 JM\mathbf e_0=\kappa(-q)^D
                  \bigl((-q^{-1})^j\bigr)_{j=0}^D,
 \qquad
 (JM)^2\mathbf e_0=\mathbf e_D,\qquad
 (JM)^3\mathbf e_0=\kappa\mathbf e_0.
 \tag{13}
\]
The middle equality uses
\(\kappa^2(-q)^D=1\). It must not be recovered by cancelling
the zero and pole in separate scalar factors of (10).

The single crossing has the equally exact formula
\[
 \boxed{\quad
 Mw(a,b)=\kappa(a^2/b)^D
       \operatorname{diag}\bigl((Q/a)^j\bigr)_{j=0}^D
                   w(b/a,b).
 \quad}
 \tag{14}
\]
This follows directly from (3) and (6). The extra diagonal
character is part of the original operator. Dropping it would
turn (8) into a false closed-family statement for arbitrary
powers or turns. At cap parameters which are integral powers
of \(Q\), this character is an actual clock power. Transporting
it by \(M\) gives the already established \(K,P_m,C_m\)
coordinates of the
[quantum continuant theorem](research_crossing_run_quantum_continuants.md);
it does not eliminate their forced source response.

Away from zeros, and only for \(0\le k<D\), the chart has the ratio
\(w_{k+1}/w_k=-b(1-aQ^k)/(qa(1-bQ^k))\).
As a function of the clock \(x=Q^k\), this ratio has numerator
and denominator degree at most one. The next section tests
this type of exact product closure for the specified off-grid
source, allowing any fixed number of additional factors.
There is no cyclic \(k=D\) equation implicit in this finite
interval ratio.

## 3. An exact three-crossing obstruction to bounded product closure

Use a new letter \(p_N\) for the scalar polynomial in
[the primitive odd-source calculation](research_odd_primitive_scalar_recurrence.md),
so it is not confused with the spectral quotient polynomial.
That calculation gives, for every \(N\ge2\),
\[
 \begin{split}
 &p_N\text{ monic of degree }D,\qquad p_N(Q)=1,\\
 &p_N(Qx)=(1-x)^2p_N(x)+x(2-x^N),\\
 &(M^3\mathbf e_0)_j
      =\kappa^3(-q)^j p_N(Q^{j+1}).
 \end{split}
 \tag{15}
\]
This is the canonical polynomial horizontal section, with its
marked forcing and cap normalization, not an arbitrary
interpolation of the \(N\) samples.

**Proposition 2.** The reduced rational function
\(p_N(Qx)/p_N(x)\) has numerator and denominator degrees at
least \(N-2\). Consequently it cannot, for arbitrarily large
\(N\), be the rational \(Q\)-shift ratio of an exact product
family of uniformly bounded shift degree.

*Proof.* Suppose a nonzero \(z\) were a common zero of
\(p_N(x)\) and \(p_N(Qx)\). Equation (15) forces \(z^N=2\).
At such a point the inhomogeneous term vanishes around the
entire \(Q\)-orbit. Thus \(p_N(Q^jz)=0\) for all \(j\),
which gives \(N\) distinct roots of a nonzero polynomial of
degree \(N-1\), a contradiction.

The only possible common zero is therefore zero. If
\(p_N(0)=0\) to order \(d\ge2\), the left side of the second
line of (15), after moving its homogeneous term, has order
at least two, whereas \(x(2-x^N)\) has order one. Hence the
common zero at zero has order at most one. The two polynomials
both have degree \(D\), so cancelling their greatest common
divisor leaves degrees at least \(D-1=N-2\). \(\square\)

Here is a concrete class covered by the assertion. Let
\[
 F_N(x)=h_N(x^N)x^{d_N}R_N(x)
       \prod_{\nu=1}^{L}
          (a_{\nu,N}x;Q)_{m_{\nu,N}}^{\epsilon_\nu},
 \tag{16}
\]
where \(h_N\) is any nonzero meromorphic invariant factor,
\(d_N\) is an integer, \(R_N\) is rational with numerator
and denominator degrees at most \(r\), and
\(\sum_\nu|\epsilon_\nu|\le L_0\).
The parameters and product lengths may depend on \(N\), but
\(r,L_0\) are fixed. Then
\[
 \frac{F_N(Qx)}{F_N(x)}
  =Q^{d_N}\frac{R_N(Qx)}{R_N(x)}
       \prod_\nu
       \left(\frac{1-a_{\nu,N}Q^{m_{\nu,N}}x}
                    {1-a_{\nu,N}x}\right)^{\epsilon_\nu}
 \tag{17}
\]
has numerator and denominator degrees at most \(2r+L_0\).
In particular \(p_N\) cannot equal (16) as a meromorphic
function once \(N>2r+L_0+2\). Multiplying by an invariant
factor \(h_N(x^N)\) does not alter this conclusion.
The same reasoning applies to any bounded collection of
analytic factorial factors whose exact \(Q\)-shift ratios
are rational of uniformly bounded degree.

This statement requires equality of the selected off-grid
functions. It does not rule out another interpolation of
the same \(N\) values, a factor with an unbounded-degree
shift ratio, or an asymptotic product approximation with
a controlled error. In particular the
[proved three-crossing factorial profile](research_three_crossing_full_coefficient_profile.md)
is consistent with Proposition 2.

The actual source has instead the fixed two-channel
homogeneous realization
\[
 \binom{p_N(Qx)}{1}
 =
 \begin{pmatrix}
   (1-x)^2&x(2-X)\\0&1
 \end{pmatrix}
 \binom{p_N(x)}{1},
 \qquad X=x^N.
 \tag{18}
\]
The second channel retains the known scalar forcing
\(2-X\), which is one on the physical orbit \(X=1\).
It cannot be erased to obtain a scalar homogeneous
product solution. Fixed-channel forced systems for
general runs and words remain possible, as in
[the source compiler](research_rational_word_local_source_system.md).

Thus (8) is a genuine cap-normalized finite transport identity,
while (15)--(18) locate the first necessary enlargement of a
bounded-product algorithm. Neither proves a nonzero geometric
closing coefficient for an arbitrary fixed short word. That
still requires a quantitative connection estimate for its
marked forced solution, including the final observation.

Replacing \(q,Q,\kappa\) by their inverses gives the corresponding
negative-crossing identities, with the input parameters left as
independent complex variables. This is coefficientwise conjugation
of the original real Newton representation, not conjugation of an
arbitrary input state.

## 4. Finite normalization check

The [focused checker](../experiments/check_polynomial_cap_chart.py)
constructs \(M\) by multiplication in the full polynomial quotient.
It checks (8), (9), (12), (14), a parameter jet at the cap, and
the actual source and forcing in (15). It includes generic
complex parameters and all three cap-orbit points, so no evaluation
of the singular ratio \(f\) is used at those points.

The [saved record](../repro/results/research-polynomial-cap-chart.json)
contains 864 finite identities at levels \(2,\ldots,10\), at
100 decimal digits, with maximum relative error below
\(1.37\cdot10^{-97}\). Source and direct dependency hashes are
recorded. These checks concern phases, endpoint normalization
and implementation; the degree obstruction is proved above.

    python3 experiments/check_polynomial_cap_chart.py --precision 100
