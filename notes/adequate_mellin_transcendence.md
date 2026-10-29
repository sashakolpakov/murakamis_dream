# The actual Mellin period is transcendental for every nontrivial adequate knot

Research theorem, 27 October 2026. The actual Fourier--Mellin section
has a bounded rational source and a specified formal source lattice.
For every nontrivial adequate knot that selected section is
transcendental over C(Q,X). This follows from the already proved
quadratic color-degree span and an elementary valuation bound for
algebraic power series, proved below without an Eisenstein theorem.

This is a theorem about the actual pointed period for a wide knot
class, including hyperbolic alternating knots. It does not identify
its geometric A-component or prove its root-value volume growth.

## 1. Algebraic power series have linearly bounded coefficient valuations

Let K be a characteristic-zero discretely valued field, with valuation
v, valuation ring R and uniformizer pi. Completeness is unnecessary.
Let

    f(X)=sum_(n>=0)c_n X^n in K[[X]]

be algebraic over K(X). Then there are constants A,B>=0 such that

    v(c_n)>=-A-Bn for all nonzero coefficients.  (1.1)

Here and below zero coefficients satisfy the bound by v(0)=infinity.

**Proof.** Choose a polynomial P(X,Z) in K[X,Z] for which
P(X,f)=0 and P_Z(X,f)!=0. Such a choice exists because the minimal
polynomial is separable in characteristic zero. Put

    m=ord_X P_Z(X,f), choose k>m,
    p(X)=sum_(n=0)^(k-1)c_n X^n,
    f=p+X^k w.

Since p-f has order at least k>m,

    ord_X P_Z(X,p)=m.

Taylor expansion gives a polynomial

    F(X,W)=X^(-m-k) P(X,p+X^k W) in K[X,W].    (1.2)

Indeed the linear term is divisible by X^(m+k). The terms of
degree j>=2 in W have exponent at least kj, and
kj-(m+k)=k(j-1)-m>0. The constant term P(X,p) is divisible
by X^(m+k) because substituting w makes the entire Taylor sum
zero. At X=0, therefore,

    F(0,W)=aW+b, a=[X^m]P_Z(X,p)!=0.

Let w_0=-b/a, which is the constant coefficient of w. Set W=w_0+V
and divide by a. The resulting polynomial has the exact form

    V+X H(X,V)=0, H in K[X,V].                  (1.3)

This is the useful normalization: all other monomials have positive
X order. Write H=sum h_(i,j) X^i V^j. Choose an integer B>=0 with

    v(h_(i,j))+B(i+1)>=0 for every nonzero h_(i,j). (1.4)

There are finitely many coefficients, so such a B exists. Under
X=pi^B x the selected series z(x)=V(pi^B x) satisfies

    z+x H_B(x,z)=0,
    H_B(x,z)=pi^B H(pi^B x,z) in R[x,z].        (1.5)

Its constant term is zero. In the coefficient recursion, the
coefficient of x^n on the right depends only on earlier coefficients
of z because of the outer factor x. Induction shows z belongs to
xR[[x]]. Thus, writing V=sum_(r>=1)v_r X^r,

    v(v_r)>=-Br.

For n>=k+1 one has c_n=v_(n-k), and hence
v(c_n)>=-B(n-k)>=-Bn. The finitely many coefficients through
c_k are covered by increasing A. This proves (1.1).

No analytic convergence and no a priori integrality of the original
coefficients is used. The truncation removes the possible singular
derivative, normalization gives one unit linear coefficient, and a
single rescaling of X makes the finite recursion integral.

## 2. Consequence for rational-function coefficients in Q

Apply the theorem to K=C(Q), first with the valuation at Q=0 and
then with the valuation at Q=infinity. For a Laurent polynomial
c_n(Q), these valuations are respectively

    v_0(c_n)=mindeg_Q c_n,
    v_infinity(c_n)=-maxdeg_Q c_n.

Consequently an algebraic f(X) with Laurent-polynomial coefficients
must satisfy

    mindeg_Q c_n>=-A_0-B_0n,
    maxdeg_Q c_n<= A_infinity+B_infinity n,
    span_Q c_n=O(n).                            (2.1)

The algebraic relation may have arbitrary complex coefficients;
their Q-valuations are zero. Thus this conclusion applies to
algebraicity over C(Q,X), not only over the rational number field.
It also covers any finite algebraic cover supplying a scalar branch
in the selected integer-power series lattice.

## 3. The actual adequate color coefficients violate this bound

The actual fixed-color functions C_n(Q) are Laurent polynomials,
and the
[adequacy proof](adequacy_and_algebraic_periods.md) establishes their
extreme degrees directly from adequate states, cabling and threading.
For an adequate diagram with c>0 crossings and state-circle counts
v_A,v_B it gives, in the q parameter,

    span_q C_n=c(n-1)^2+(v_A+v_B-2)(n-1).

The [actual Q-polarization](fourier_mellin_actual_source.md) has
Q=q^2 and C_n even in q, so

    span_Q C_n=(1/2)c(n-1)^2
                    +(1/2)(v_A+v_B-2)(n-1).    (3.1)

In particular it has a strictly positive quadratic coefficient.
For a reduced connected alternating diagram this simplifies to
span_Q C_n=c n(n-1)/2. The zero-framing monomial does not change
the span.

Choose the fixed n_0 of the actual Fourier--Mellin construction and
retain its exact selected section

    Z(Q,X)=sum_(n>=n_0) C_n(Q) X^n.              (3.2)

If Z were algebraic over C(Q,X), equation (2.1) would bound its
coefficient spans linearly. This contradicts (3.1) for every
nontrivial adequate knot. We have therefore proved

    Z(Q,X) is transcendental over C(Q,X).       (3.3)

Subtracting or adding any fixed initial-color polynomial preserves
algebraicity. Thus the conclusion holds for every fixed starting
color, including the start-one generating period.

## 4. The precise source/lattice conclusion

The actual bounded-source identity is

    P^M Z=B,
    Z in X^(n_0) C(Q)[[X]],                     (4.1)

where B is the fixed nonzero Laurent source from finitely many
small colors. The source-lattice condition makes this solution
unique, by the leading-coefficient argument of the Fourier--Mellin
construction. Hence no scalar section on a finite algebraic cover,
satisfying this actual source and this formal lattice, can replace Z.
The selected whole period is necessarily transcendental.

There is a useful operator consequence. Every nonzero actual
Q-operator of a nontrivial adequate knot has positive generic
Y-exponent span. Otherwise all its Y exponents would be a single
m, and its Fourier image would have the form A(Q,X)S^m with
A!=0. Equation (4.1) would make S^m Z=B/A rational, and hence
Z rational, contradicting (3.3). Thus the actual Mellin source
object has positive difference order for this whole knot class;
no artificial factor is needed to create that order. This is
not a claim about the operator's specialized symbol at Q=1.

This does not contradict algebraicity of the underlying equations,
gluing place, comparison torsor or connection. Their marked periods
can be transcendental. Nor does it contradict rationality of the
root fibers: the original
[cyclotomic residue construction](cyclotomic_mellin_residue.md) gives
a rational function at each Q_N whose degree grows with N.

The assertion is not generic affine nonsplitting without the lattice.
A rational or algebraic particular solution outside X^(n_0)[[X]]
could coexist with the selected transcendental solution, differing
by a homogeneous solution. We have not excluded that possibility.
The theorem excludes a pointed algebraic splitting compatible with
the actual source lattice and coefficient cut.

Finally, quadratic degree span gives no lower bound for a specified
root value. Cancellation can still occur at Q_N. The exact identity
<K>_N=[X^N]Z(Q_N,X), or its infinity-residue version, remains the
original volume target. No exponential regulator estimate is inferred
from transcendence alone.

[Exact valuation-normalization audit](../experiments/audit_adequate_mellin_transcendence.py).
[Results](../experiments/adequate_mellin_transcendence_results.json).
