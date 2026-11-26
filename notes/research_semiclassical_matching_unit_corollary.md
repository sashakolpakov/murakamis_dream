# Near-identity radical transport in the full semiclassical jet norm

The exact matching unit of [M] is near the identity, in both
directions, when each normalized first derivative is divided by
the level. This changes neither the physical algebra nor the original
closing functional.

Use all notation and hypotheses of [M]: \(N\ge2\),
\(m=\lfloor N/2\rfloor\), \(\eta=(-1)^{N-1}\), and a fixed finite
multigraph \(\mathcal E\) of actual same-index Newton connections
between vertices in \(I\) subjected to the original traces.
Only those vertices are reduced modulo \(P_N\). All free-boundary
variables and other attachments remain ordinary.

On the full physical algebra give \(f\) the norm
\[
 \|f\|_{\rm sc}^{\,2}
 =\sum_{a<m}\left(|f(c_a)|^2+
       \left|\frac{j_a(f)}N\right|^2\right)
       +\mathbf1_{N\ {\rm odd}}|f(-2)|^2,\qquad
 j_a(f)=\eta(4-c_a^2)f'(c_a).
 \tag{1}
\]
Use its Hilbert tensor norm on \(I\). Every value and first normal
remains present, including the odd simple value. In comparison with
the unscaled full-jet norm of [M],
\[
 N^{-|I|}\|F\|_{\rm j}\le\|F\|_{\rm sc}\le\|F\|_{\rm j}.
 \tag{2}
\]

Let \(U=\prod_{e\in\mathcal E}(1+V_e)\) be the exact unit of [M].
Writing \(\mathfrak M\) for the matchings, including the empty one, set
\[
 \epsilon_N=\sum_{\substack{M\in\mathfrak M\\M\ne\varnothing}}
                     (2/N)^{|M|}.
\]
Then
\[
 \boxed{\ 
 \|M_U-I\|_{\rm sc},\ \|M_{U^{-1}}-I\|_{\rm sc}
 \le\epsilon_N
 \le(1+2/N)^{|\mathcal E|}-1=O_{\mathcal E}(N^{-1}).
 \ }
 \tag{3}
\]
Here \(M_f\) denotes multiplication. Indeed the normalized radical
coupon \(\delta_a\) sends the scaled local coordinates \((v,n)\) to
\((0,v/N)\). Thus \(\|M_{\delta_a}\|_{\rm sc}=N^{-1}\).
For \(e=vw\), the exact formula
\[
 V_e=\sum_{a,b<m}\frac{W_{ab}}{G_{ab}}\,
                  \delta_a^{(v)}\delta_b^{(w)},\qquad
 G_{ab}\ge1,\quad |W_{ab}|\le4m
\]
and orthogonality of the physical-color blocks give
\(\|M_{V_e}\|_{\rm sc}\le4m/N^2\le2/N\).
The full matching expansions for \(U\) and \(U^{-1}\) in [M],
with the empty matching removed, prove (3).
Odd simple slots give zero edge action. Parallel edges obey the same
matching exclusion; a chosen loop has zero radical term.

Consequently the actual full and low sources \(F=UF_<\), with every
signed crossing power and arbitrary joint attachment retained, satisfy
\[
 \|F-F_<\|_{\rm sc}\le\epsilon_N\|F_<\|_{\rm sc},\qquad
 (1+\epsilon_N)^{-1}\|F_<\|_{\rm sc}
 \le\|F\|_{\rm sc}\le(1+\epsilon_N)\|F_<\|_{\rm sc}.
 \tag{4}
\]
The condition number of \(M_U\) is at most \((1+\epsilon_N)^2\).
All statements also hold coefficientwise in the ordinary free
variables and their derivatives, or after tensoring an independent
exterior Hilbert space.

The original row remains \(\ell=\bigotimes_{v\in I}\phi_N\).
In (1) its single-vertex row is
\((-\eta c_a,N)_{a<m}\), together with \(1\) at the odd simple node.
Hence
\[
 \|\ell\|_{\rm sc}^2
   =\left(mN^2+\sum_{a<m}c_a^2+\mathbf1_{N\ {\rm odd}}\right)^{|I|},
 \qquad
 \frac{\|\ell M_U-\ell\|_{\rm sc}}{\|\ell\|_{\rm sc}}
       \le\epsilon_N.
 \tag{5}
\]
The exact observation is still \(\ell(F)=(\ell M_U)(F_<)\).
Its comparison with the unchanged low closing is only the absolute
estimate
\[
 |\ell(F)-\ell(F_<)|
 \le\epsilon_N\|\ell\|_{\rm sc}\|F_<\|_{\rm sc}.
 \tag{6}
\]
In particular (6) is not a relative scalar estimate after cancellation.

For completeness, the actual signed power \(R^n\) acts on a double
block by its unit-modulus value times the shear
\[
 \begin{pmatrix}1&0\\
 i\eta n(d-2a)\sin((2a+1)\pi/N)/N&1
 \end{pmatrix}.
\]
Thus \(\|M_{R^{\pm n}}\|_{\rm sc}\le1+|n|\). Fixed signed powers,
as well as \(U\), preserve the exponential rate of the raw full-jet
norm; neither assertion supplies a nonzero original scalar or a
selected geometric contribution. No further turn is asserted to
preserve this fixed-network radical decomposition.

## Direct source

[M: Full radical matching unit transport](research_full_radical_matching_unit_transport.md),
SHA256 437867f73282cf09d7bd7b7e9b03759401cf6e96733f9e6116854dc867e40112.
