# Full crossing spectra distinguish the two actual normal paths

Independent proof and audit, 27 October 2026. The whole Gamma
comparison transports actual scalar source factors. It cannot be
extended to a scalar-adjusted similarity of the two checked crossing
matrices on the same finite tensor fiber. This failure holds for every
level, including arbitrary nondiagonal gauges. It does not exclude
transport of the base, a relative kernel, or an enlarged normal module.

The local coefficient comparison is
[the actual crossing calculation](actual_crossing_q_normal_meridian_ratio.md).
The compatible constructive statement is the
[whole bulk response](quantum_normal_crossing_bulk_response.md).

## 1. Exact spectra and the general obstruction

Write \(n=N-1\). On the highest-weight basis use
\[
 K u_i=q^{\alpha-2i}u_i,\qquad Fu_i=u_{i+1},\qquad
 Eu_i=[i]_q[\alpha-i+1]_q u_{i-1}.
\]
The actual full positive checked crossing, including its common
Cartan factor, has the following generic eigenvalues:
\[
 r_j(q,\alpha)=(-1)^j
 q^{\alpha^2/2-j(2\alpha-j+1)},\qquad 0\le j<N.       \tag{1}
\]
Here generic means away from the explicitly finite eigenvalue
collision and highest-weight degeneracy loci.

There are two different multiplicity formulas:

* For the ordinary integral \(N\)-color, \(\alpha=n\) and generic
  moving \(q\), the multiplicity of \(r_j\) is \(2(n-j)+1\).
* At \(q_0=e^{\pi i/N}\), for a generic typical \(N\)-color with
  \(\alpha=n+b\), the multiplicity of every \(r_j\) is \(N\).

These multiplicity lists are different for every \(N\ge2\). Therefore
the moving-\(q\) integral crossing and the fixed-root typical crossing
are not similar, even after either is multiplied by any nonzero
scalar function. The conclusion survives meromorphic or ramified
changes of matrix basis: an equality of such matrices would imply
equality over their common generic fraction field, where the
eigenvalue multiplicities disagree. Retaining an additional common
Cartan, zero-framing, or peripheral scalar cannot change this argument.

Here is a direct proof of both formulas. At total index \(j<N\)
the vector
\[
 v_j=\sum_{a=0}^j c_a u_a\otimes u_{j-a},\qquad c_0=1,
\]
in the kernel of \(\Delta E=E\otimes K+1\otimes E\) is unique for
generic parameters. Successive coefficient cancellation gives
\[
 c_j=(-1)^j q^{-j(\alpha-j+1)}.                    \tag{2}
\]
The checked crossing preserves this highest vector line. To compute
its eigenvalue, inspect the coefficient of \(u_0\otimes u_j\).
In the actual \(Pq^{H\otimes H/2}\sum_k(\cdots)E^k\otimes F^k\),
only the input \(u_j\otimes u_0\) with \(k=0\) can contribute.
Its coefficient is \(c_jq^{\alpha^2/2-\alpha j}\), which is (1).

For generic moving \(q\) and integral \(\alpha=n\), the string
generated from \(v_j\) by \(\Delta F\) has highest weight \(2n-2j\)
and length \(2(n-j)+1\). Indeed
\[
 E F^r v_j=[r]_q[2n-2j-r+1]_qF^{r-1}v_j
\]
proves nonvanishing through its stated length. A further nonzero
vector would be a highest vector of negative integral weight; its
successive \(F\)-vectors would never terminate by the same identity,
contradicting finite dimension. The distinct generic Casimir
eigenvalues separate these strings. Their dimensions sum to \(N^2\).

At \(q_0\) and generic \(\alpha=n+b\), each string instead has exactly
length \(N\). The displayed \(EF^r\) factors are nonzero for
\(1\le r<N\), whereas \((\Delta F)^N=0\): the root quantum-binomial
formula leaves only the two \(N\)-th powers, both zero on the actual
head. Its generic Casimir eigenvalues are proportional to
\(q_0^{2\alpha-2j+1}+q_0^{-2\alpha+2j-1}\); as functions of the
generic meridian they are distinct for \(0\le j<N\).
Thus these \(N\) independent strings exhaust the \(N^2\)-dimensional
tensor product. Since the checked crossing commutes with the
coproduct, its eigenvalue (1) has multiplicity \(N\).

## 2. Literal first-normal diagnostics

Set \(c=2\pi i\), \(H_0=c/N\). The matched first-normal parameters
may be written
\[
 q=q_0(1+\epsilon/N),\quad M_{\mathrm{col}}=-q^N=1+\epsilon,
 \qquad q=q_0,\quad M_{\mathrm{root}}=1+\epsilon,\quad \epsilon^2=0 .
\]
These are the tangents of
\(H=H_0/(1-b/N)\), \(M_{\mathrm{col}}=e^{Hb/2}\) and
\(M_{\mathrm{root}}=e^{H_0b/2}\), with \(\epsilon=cb/(2N)\).

To make the normalization explicit, let \(R_0\) have the common
Cartan \(q^{\alpha^2/2}\) removed, put \(x=q^\alpha=-M/q\), and use
\[
 \mathcal R=x^nR_0 .
\]
This is exactly the same-auxiliary zero-framing crossing
\(R/\theta_{\mathrm{aux}}\), since
\(\theta_{\mathrm{aux}}=q^{\alpha^2/2-n\alpha}\).
At \(N=2\),
\[
 \operatorname{Tr}\mathcal R_{\mathrm{col}}=3q-q^{-1}
       =4q_0+\epsilon q_0,
\]
\[
 \operatorname{Tr}\mathcal R_{\mathrm{root}}
       =2q_0(M+M^{-1})=4q_0+O(\epsilon^2).       \tag{3}
\]
Thus even the first-normal traces differ in this specified
normalization. An arbitrary first-normal scalar could change this
one trace; the generic multiplicity theorem does not have that
normalization dependence.

There is also an independent module invariant. With
\(\gamma=(-1)^{N-1}\), the actual \(K^N\) matrices are
\[
 K_{\mathrm{col}}^N
   =\gamma\,\operatorname{diag}
       (1+\epsilon(n-2j))_{j=0}^{N-1},\qquad
 K_{\mathrm{root}}^N=\gamma(1+N\epsilon)I .
\]
Their trace derivatives are \(0\) and \(\gamma N^2\).
The moving-\(q\) first normal has a nonzero traceless component;
the fixed-root one is scalar. Thus a strict module intertwiner
retaining \(K\) already fails before forming a whole word.

At \(b=-1\), the endpoint alias in
[the coefficient audit](actual_crossing_q_normal_meridian_ratio.md)
gives an additional elementary failure of sparse diagonal transport:
the root coefficient with input \(i=N-1,j=0,k=1\) contains
\(1-e^{-c}=0\), whereas the color coefficient contains
\(1-e^{-cN/(N+1)}\ne0\). The root and color endpoint zero divisors
are different. This is compatible with the folded, two-chart scalar
source-factor comparison, which is not a crossing intertwiner.

## 3. Exact verification and the constructive scope

[The independent script](../experiments/audit_crossing_normal_spectra.py)
assembles the literal balanced checked crossing in its conserved
total-index blocks. It computes all power traces and recovers the
characteristic polynomial by Newton identities over finite fields
and their dual numbers. It compares generic integral, generic
root-meridian, integral first-normal, and root first-normal matrices
at \(N=2,\ldots,8\): 840 exact characteristic coefficients pass.
It also checks (3) and the two \(K^N\) trace derivatives.
The full output is
[the saved exact audit](../experiments/crossing_normal_spectra_results.json).

The positive result that remains available is the full-source
bulk insertion theorem. Its exact source factor is
\[
 W_{\mathrm{aux}}=\frac1N x^{n\kappa}
    Q^{n\sum_{\mathrm{closed}}i}\prod_t r_{0,t},
 \qquad \kappa=\operatorname{writhe}-b_{\mathrm{strands}}+1 .
\]
The ordinary/auxiliary adapter
\(q^{Nn\kappa}(Q^N)^{\sum i}\) removes the pivot-dependent
linear response. Hence the remaining insertion is
\((\mathcal E-1)\mathcal A\), including the constant
\(c\kappa/2\) of the marked whole action. On a flattened
critical block it is \(-S_{\mathrm{geo}}/c\). These source and
constant signs agree directly with the literal adapter.
This proves a local formal block response; it supplies neither
a same-fiber crossing similarity nor a selected global period.
